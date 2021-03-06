import os

from flask import Flask
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

# Instantiate the db
db = SQLAlchemy()
toolbar = DebugToolbarExtension()


def create_app(script_info=None):
    # Instantiate the app
    app = Flask(__name__)

    # Enable CORS
    CORS(app)

    # Set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # Set up extensions
    db.init_app(app)
    toolbar.init_app(app)

    # Register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    # Shell context for flask cli
    @app.shell_context_processor
    def make_shell_context():
        return {'app': app, 'db': db}

    return app
