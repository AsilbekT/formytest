from flask import Flask
from .site.routes import site
from .search.routes import search


def create_app():
    app = Flask(__name__)

    # registering the modules
    app.register_blueprint(site)
    app.register_blueprint(search)

    return app
