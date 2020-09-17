SHELL := /bin/bash
BASE := $(shell /bin/pwd)


# Local Env for Developer
reset:
	rm -rf build dist *.egg-info venv

init:
	python -m venv $(BASE)/venv
	source $(BASE)/venv/bin/activate; \
		pip install --upgrade pip; \
		pip install -r $(BASE)/requirements.txt;

test:
	source $(BASE)/venv/bin/activate; \
		pytest -s

# Build python package
pip:
	rm -rf build dist *.egg-info
	python setup.py sdist bdist_wheel

# This requires testpypi setting in ~/.pypirc file setup
test_upload:
	twine upload --repository testpypi dist/*

# This requires pypi setting in ~/.pypirc file setup
upload:
	twine upload --repository pypi dist/*
