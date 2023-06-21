#---------------------------
#Run unit tests (default rule)
#---------------------------
test:
	FLASK_ENV=test pytest job_prompter -s


#---------------------------
#Sort imports and format code
#---------------------------
format-isort:
	isort job_prompter

format-black:
	black job_prompter

format: format-black format-isort


#---------------------------
#Check code style
#---------------------------
# Check code style
lint:
	flake8 

#---------------------------
#Prepare virtual environment
#---------------------------
venv-create:
	python3 -m venv env

venv: venv-create
	@echo "\nUse '. env/bin/activate' to activate and 'make install' to install all dependencies"


#---------------------------
#Install dependencies
#---------------------------
deps-pre:
	pip install pip-tools

deps-compile:
	pip-compile requirements.in

deps-install:
	pip-sync

# Recalculate and install dependencies
deps: deps-pre deps-compile deps-install

# Install dependencies
install: deps-pre deps-install


#---------------------------
#Run backend server
#---------------------------
server-dev:
	gunicorn -e FLASK_ENV=development -c gunicorn-dev.cfg.py wsgi

server-prod:
	gunicorn -e FLASK_ENV=production -c gunicorn.cfg.py wsgi


#---------------------------
#Database migrations
#---------------------------
db-migrate:
	alembic revision --autogenerate -m 'Change summary'

db-upgrade:
	alembic upgrade 'head'

db-downgrade-1:
	alembic downgrade -1