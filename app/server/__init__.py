import logging, os

from flask import Flask
from util.cred_handler import get_secret


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=get_secret('SECRET_KEY')
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    app.logger.setLevel(logging.INFO)
    
    app.logger.info("Registering blueprints")

    from . import endpoint
    app.register_blueprint(endpoint.bp)

    return app
