.DEFAULT_GOAL := help

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

setup: ## initial package installation
	pipenv install
	pipenv install --dev

env: ## activate working environment/shell.
	pipenv shell

docs: ## generate Sphinx HTML documentation
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

test: ## runs test with pytest with default Python
	pytest -v

test-all: ## run tests on every Python version with tox
	tox