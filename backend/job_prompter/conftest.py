"""
This file defines fixtures and other shared objects
that can be used across multiple test files or modules.
"""
import pytest

from job_prompter import config
from job_prompter.extensions import db as _db
from job_prompter.factory import create_app


@pytest.fixture(scope="session")
def app():
    job_prompter_app = create_app()

    job_prompter_app.config["SERVER_NAME"] = "localhost"

    return job_prompter_app


@pytest.fixture(scope="session")
def db(app):
    """Session-wide test database."""

    assert (
        config.FLASK_ENV == "test"
    ), "Unit tests have to be executed in `test` environment"
    assert (
        "localhost/" in config.SQLALCHEMY_DATABASE_URI
    ), "Unit tests have to be executed against local DB"

    with app.app_context():
        _db.Model.metadata.drop_all(_db.engine)
        _db.Model.metadata.create_all(_db.engine)

        yield _db


@pytest.fixture
def session(db):
    """Start a session with a savepoint then rollback to it on test teardown"""
    db.session.begin_nested()

    yield db.session

    db.session.rollback()


@pytest.fixture
def _client(app, session):
    return app.test_client()
