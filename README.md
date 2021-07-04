# Flask-Postgres base

## Overview

A basic repository containing the necessary framework files for a skeleton app using Docker, Flask, and Postgres as a database. Gunicorn is used as the WSGI server, rather than the native Flask development server. It also supports asyncronous task management using Celery with a Redis backend and Rabbit MQ broker.

Nginx is configured as a reverse proxy for the application.

It also includes native support for Alembic to create database migrations. These migrations will automatically be run everytime docker-compose is run, to ensure that the included databaes is kept up to date.

A secret handling function is also included, that can make use of either secrets contained in a cred.json file, or taken from environment variables.

Additionally, by default, auto-reload is enabled on changes to the contents of the app folder, to allow for easy development.

## Basic Usage

This repository is meant to be used as a template for further development. Firstly, clone this repository, and enter into it:

```bash
git clone https://github.com/Hijerboa/flask-postgres-base.git
cd flask-postgres-base
```

Copy app/util/cred_example.json to app/util/cred.json. This contains the connection string for the included database.

Next, build and run the docker containers:

```bash
docker-compose build
docker-compose up
```

Visit localhost:1337 in your browser, and you should see the root page of the application.

From this point, you can use this repository to develop as you would normally for a Flask applicaiton. Flask specific files are meant to be located in the app/server folder, with database migrations located in the app/db/migrations folder.

## Adding Endpoints

Likely, you'll want to add additional endpoints to the Flask application. By default, this applicaiton includes a single endpoint contained in one blueprint, located in app/server/endpoint.py. All endpoints must be imported and included in app/server/\_\_init\_\_.py.

While it is possible to include endpoints in the flask \_\_init\_\_.py file, this is not recommended. It is recommended to take advantage of Flask's built in blueprint system. More information about this blueprint system can be found in Flask's [official documenation](https://flask.palletsprojects.com/en/2.0.x/blueprints/)

## Handling Secrets

It is always important to not store any secrets in a Github repository, and even more important to not hard code those secrets. For this reason, this repository also includes a basic secret handling function.

It can pull secrets from either a cred.json file (located at the same location the cred_example.json is located), or from environment variables. An example of it's usage can be found in both app/db/migrations/env.py, and in app/server/\_\_init\_\_.py. In the former, the connection string for the database is pulled from the cred.json file you created in the initial setup. In the later, the SECRET_KEY environment variable is pulled and passed to the program by the cred_handler function. Both of these methods are valid ways to store secrets.

When a secret is pulled the first time, it will be cached in memory for a faster response in subsequent requests.

## Logging

Like any good framework, Flask includes logging, specifically uses Python's built in logging. An example of using logging is present in both app/server/\_\_init\_\_.py, and in app/server/endpoint.py. In app/server/\_\_init\_\_.py, the log level of the application is set to be info, however this can be changed easily.

## Making Migrations

You will notice that this docker-compose file creates three containers: the container the Flask app runs in, the database container, and a third container known as "migrations". This container runs initially at startup, and performs any migrations necessary to update the database structure.

This container makes use of Alembic's migration functionality. Normally, some configuration is needed to make these migrations work, but that has all been setup in this repository. All you need to do is install alembic to your development system:

```bash
sudo apt install alembic
```

Then, navigate to app/db, and then run

```bash
alembic revision -m "Migration name"
```

This will generate a new python file under the migrations folder, which you can add upgrade and downgrade syntax using SQL Alchemy syntax.

More information on this process can be found on Alembic's [official documenation](https://alembic.sqlalchemy.org/en/latest/tutorial.html#create-a-migration-script)

## Async Task Handling

This project uses a relatively standard celery setup. Tasks are defined in the app/server/tasks.py by default. It is recommended you add tasks in this location.

An example of an async task and it's usage is provided. The root endpoint (located in app/server/endpoint.py) demonstrates how an async task can be handled. Notice how when visiting the page, a response is recieved instantly, but the task is queued by the celery workers and completed 2 seconds later. No matter how many times you reload the page, it still responds instantly, and even as the tasks pile up, the workers will handle it.

Further docs on celery can be found on the [official documentation](https://docs.celeryproject.org/en/stable/index.html)

### Scaling Celery Workers

Scaling celery workers is simple with docker-compose. By default, only a single worker is created, but if more are required, simply edit the "scale" attribute of the celery-worker entry in docker-compose.yml

### Periodic Tasks

Also included in this template is a celery-beat container. Celery beat is used to schedule tasks on a reoccuring, regular basis. Under no circumstances should you scale the celery beat container, as this will quickly devolve into madness.

An example scheduled task is included in app/server/tasks.py that is called every 10 seconds. Further documentation can be found at the [official documenation](https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html)
