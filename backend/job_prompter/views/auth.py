from flask import Blueprint

from job_prompter import config

auth_bprint = Blueprint("auth", __name__)


@auth_bprint.route("/api")
def index():
    return {"user": "jeff"}
