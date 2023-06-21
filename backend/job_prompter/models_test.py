from job_prompter.fixtures import create_user
from job_prompter.models import User


def test_user_creation(session):
    user = create_user()
    session.flush()
    db_user = User.query.first()

    assert user == db_user
