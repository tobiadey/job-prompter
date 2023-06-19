# Prepare virtual environment
venv-create:
	python3 -m venv env

venv: venv-create
	@echo "\nUse '. env/bin/activate' to activate and 'make install' to install all dependencies"

# Run frontend server
run-client:
	@echo "no client yet"

# Run backend server
run-server:
	python3 -m wsgi

# Run unit tests (default rule)
test:
	python3 -m pytest

# Install dependencies
install:
	pip install -r requirements.txt

# Sort imports and format code
format-isort:
	isort app

format-black:
	black app

format: format-black format-isort

# Check code style
lint-flake8:
	flake8 app

lint-types:
	mypy --package app

lint: lint-types lint-flake8