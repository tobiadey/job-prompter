import os

# JOB_PROMPTER database with development defaults
SQLALCHEMY_DATABASE_URI = os.environ.get(
    "JOB_PROMPTER_DB_URL", "postgresql://user:user@localhost/job_prompter_dev"
)
