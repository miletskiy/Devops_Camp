# -*- Makefile -*-
SHELL=/bin/bash

# constants
PROJECT_NAME=Metrics
PYTHON=python

.PHONY: run pip test shell clean clean-pyc
.DEFAULT_GOAL := run

run:
	@echo Starting $(PROJECT_NAME)...
	$(PYTHON) metrics.py

pip:
	pip install -r requirements.txt

shell:
	@echo Open shell...
	ipython

clean: clean-pyc

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.pytest_cache' -exec rm -fr {} +
