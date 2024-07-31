from .. import app

from flask import Blueprint, render_template
from taskl import TaskWarrior

projects_blueprint = Blueprint('projects', __name__)


@projects_blueprint.route('/projects')
def projects():

    tasks = TaskWarrior()
    projects = tasks.get_projects()
    
    project_tasks = {}
    for project in projects:
        project_tasks[project] = tasks.get_project_tasks(project, only_pending=False)

    return render_template('projects.html.jinja2', projects=projects, project_tasks=project_tasks)
