VENV?=.venv
PYTHON?=$(VENV)/bin/python3
PIP?=$(PYTHON) -m pip

docker-up:
	docker-compose up airflow-init
	docker-compose up -d

docker-down:
	docker-compose down --volumes --rmi all

clean: docker-down
	@echo "removing recursively: *.py[cod]"
	find . -type f -name "*.pyc" -exec rm '{}' +
	find . -type d -name "__pycache__" -exec rm -rf '{}' +
	find . -type d -name ".pytest_cache" -exec rm -rf '{}' +
	find . -type d -name "*.egg-info" -exec rm -rf '{}' +
	rm -rf $(VENV) .pybuilder
	rm poetry.lock
	@echo "\033[31mNow, run the \`exit\` command to close the shell session created by poetry!\033[0m"