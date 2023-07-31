VENV?=.venv
PYTHON?=$(VENV)/bin/python3
PIP?=$(PYTHON) -m pip

run:
	@echo "\33[0;32m Reddit collector is Running!\033[0;32m"
	$(PYTHON) src/main.py

install-poetry:
	@if ! command -v poetry &>/dev/null; then \
		echo "Installing poetry..."; \
		pip3 install poetry; \
	fi

venv: install-poetry
	@echo "Creating the venv..."
	@poetry install
	$(PIP) install --upgrade pip
	@echo "Starting the virtual environment..."
	@poetry shell

clean:
	@echo "removing recursively: *.py[cod]"
	find . -type f -name "*.pyc" -exec rm '{}' +
	find . -type d -name "__pycache__" -exec rm -rf '{}' +
	find . -type d -name ".pytest_cache" -exec rm -rf '{}' +
	find . -type d -name "*.egg-info" -exec rm -rf '{}' +
	rm -rf $(VENV) .pybuilder
	@echo "\033[31mNow, run the \`exit\` command to close the shell session created by poetry!\033[0m"