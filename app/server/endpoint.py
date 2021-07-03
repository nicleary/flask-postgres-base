import functools
from server.tasks import this_is_a_task

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)

bp = Blueprint('endpoint', __name__, url_prefix='/')

@bp.route('/', methods=(['GET']))
def main_page():
    current_app.logger.info("wow you hit that page")
    hello_there = this_is_a_task.delay()
    return "Hello there, this is the main page."