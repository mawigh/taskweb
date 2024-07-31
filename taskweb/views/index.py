from flask import Blueprint, url_for, redirect

index_blueprint = Blueprint('index', __name__)


@index_blueprint.route('/')
def index():

    return redirect(url_for('projects.projects'))
