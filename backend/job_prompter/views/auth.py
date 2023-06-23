import logging
from job_prompter.extensions import db
from job_prompter.models import User
from flask import Blueprint, redirect, url_for, request, jsonify, abort
from werkzeug.exceptions import Conflict
from flask_session import session

# from job_prompter import config

auth_bprint = Blueprint("auth", __name__)
logger = logging.getLogger(__name__)


@auth_bprint.route("/authenticate_user", methods=["POST"])  # rename to /login
def authenticate_user():
    email = request.json["email"]
    logger.info(email)
    user_exists = User.query.filter_by(email=email).first()
    logger.info(user_exists)

    if user_exists:
        abort(409)

    new_user = User(
        first_name=request.json["given_name"],
        last_name=request.json["family_name"],
        email=email,
        password="xxx",
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify(
        {
            "id": new_user.id,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "email": new_user.email,
            "password": new_user.password,
        }
    )
