"""Flask Application Factory"""
from flask import Flask


def create_app(app_name="Sommit Admin", config_name=None):
    """Create the Flask App and plug in configuration, services, routes, template filters and jobs."""
    app: Flask = Flask(app_name)

    @app.get("/ping")
    def ping():
        return "pong"

    return app
