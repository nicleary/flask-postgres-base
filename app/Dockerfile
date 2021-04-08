FROM python:3.8-slim-buster

EXPOSE 5000

WORKDIR /app

RUN apt-get update \
    && apt-get -y install netcat gcc postgresql libpq-dev python-dev \
    && apt-get clean

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app
CMD python3 migrations.py
CMD python3 server/app.py