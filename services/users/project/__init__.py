import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from project.api.users import users_blueprint

# Instantiate the db
db = SQLAlchemy()


def create_app(script_info=None):
    # Instantiate the app
    app = Flask(__name__)

    # Set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # Set up extensions
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(users_blueprint)

    # Shell context for flask cli
    @app.shell_context_processor
    def make_shell_context():
        return {'app': app, 'db': db}

    return app
