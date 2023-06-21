from job_prompter.models import User
from job_prompter.fixtures import create_user


def test_user_creation(session):
    user = create_user()
    session.flush()
    db_user = User.query.first()

    assert user == db_user
