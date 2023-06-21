from job_prompter.extensions import db
from job_prompter.models import User

EXAMPLE_USER = {
    "first_name": "jeff",
    "last_name": "king",
    "email": "jking@gmail.com",
    "password": "hash254",
}


def create_user(**kwargs):
    defaults = dict(
        first_name="jeff", last_name="king", email="jking@gmail.com", password="hash254"
    )

    user = User(**{**defaults, **kwargs})
    db.session.add(user)
    return user
