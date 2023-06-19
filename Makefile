#---------------------------
#Linting on API
#---------------------------
# Sort imports and format code
format-isort:
	isort api

format-black:
	black api

format: format-black format-isort

# Check code style
lint-flake8:
	flake8 api

lint-types:
	mypy --package api

lint: lint-types lint-flake8


#---------------------------
#Linting on Client
#---------------------------