VENV?=.venv
PYTHON?=$(VENV)/bin/python3
PIP?=$(PYTHON) -m pip

up: docker-up
	@echo "\33[0;32m Apache-airflow is Running!\033[0;32m"

docker-up:
	docker-compose up airflow-init
	docker-compose up -d

docker-down:
	docker-compose down --volumes --rmi all

clean: docker-down
	@echo "\33[0;32m Apache-airflow is not Running!\033[0;32m"