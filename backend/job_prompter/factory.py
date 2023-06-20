import os

from flask import Flask, Request, g, got_request_exception, request

from werkzeug.middleware.proxy_fix import ProxyFix

from job_prompter.extensions import db


def register_views(app):
    """Import and register all view functions"""
    from job_prompter.views.auth import auth_bprint

    app.register_blueprint(auth_bprint, url_prefix="/")


def create_app():
    # Root directory
    instance_dir = os.path.normpath(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..")
    )

    # Initialise the application
    app = Flask("job_prompter", instance_path=instance_dir)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_port=1)

    # Load config module
    app.config.from_object("job_prompter.config")

    # Initialise views
    register_views(app)

    # Load SQLAlchemy
    # db.init_app(app)

    return app
