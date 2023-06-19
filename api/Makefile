# Prepare virtual environment
venv-create:
	python3 -m venv env

venv: venv-create
	@echo "\nUse '. env/bin/activate' to activate and 'make install' to install all dependencies"

# Run backend server
run-server:
	python3 -m flask run

# Run unit tests (default rule)
test:
	python3 -m pytest

# Install dependencies
install:
	pip install -r requirements.txt

