"""
Typing Speed Measurement and Accuracy Test System
Flask Application Factory
"""
import os
from flask import Flask


def create_app():
    """
    Create and configure the Flask application.
    Sets up template and static folder paths,
    and registers the main blueprint.
    Returns the configured Flask app instance.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))

    app = Flask(__name__,
                template_folder=os.path.join(base_dir, '..', 'templates'),
                static_folder=os.path.join(base_dir, '..', 'static'))

    from .routes import main
    app.register_blueprint(main)

    return app