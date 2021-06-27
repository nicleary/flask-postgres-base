import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('endpoint', __name__, url_prefix='/')

@bp.route('/', methods=(['GET']))
def register():
    return "Hello there, this is the main page."