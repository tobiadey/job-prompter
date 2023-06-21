from job_prompter.extensions import db
from job_prompter.models import User


def create_user(**kwargs):
    defaults = dict(
        first_name="Jeff", last_name="King", email="jking@gmail.com", password="hash254"
    )

    user = User(**{**defaults, **kwargs})
    db.session.add(user)
    return user
