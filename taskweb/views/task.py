from .. import app

from flask import Blueprint, render_template
from taskl import TaskWarrior

task_blueprint = Blueprint('task', __name__)


@task_blueprint.route('/task/<uuid:task_uuid>/')
def projects(task_uuid):

    task_uuid = str(task_uuid)

    taskw = TaskWarrior()
    task = taskw.get_task(task_uuid)

    return render_template('task.html.jinja2', task=task.__dict__)
