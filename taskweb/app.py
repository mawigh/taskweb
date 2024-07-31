from flask import Flask

# blueprints
from .views.index import index_blueprint
from .views.projects import projects_blueprint

app = Flask(__name__)
app.register_blueprint(index_blueprint)
app.register_blueprint(projects_blueprint)
