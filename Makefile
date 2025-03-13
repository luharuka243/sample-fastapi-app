# Makefile
SHELL = /bin/bash

.PHONY: typecheck bandit format lint clean

# Do the static type check
typecheck:
	@echo "Running mypy..."
	mypy src model.py --config-file pyproject.toml

bandit:
	@echo "Running bandit...."
	bandit -r src model.py

# Format the code using Black and isort
format:
	@echo "Formatting code with Black..."
	black --config pyproject.toml src model.py
	@echo "Sorting imports with isort..."
	isort src model.py --sp pyproject.toml
	@echo "Formatting done."

# Lint the code using Flake8
lint:
	@echo "Linting code with Flake8..."
	flake8 src model.py --exclude venv --ignore E501,W503 --config pyproject.toml || true

clean:
	@echo "Cleaning ......."
	find . -type f -name "*.DS_Store" -ls -delete
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
	find . | grep -E ".pytest_cache" | xargs rm -rf
	find . | grep -E ".ipynb_checkpoints" | xargs rm -rf
	find . | grep -E ".mypy_cache" | xargs rm -rf
	rm -rf .coverage*

# Combine format and lint
all: typecheck bandit format lint clean
