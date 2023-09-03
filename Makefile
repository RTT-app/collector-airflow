VENV?=.venv
PYTHON?=$(VENV)/bin/python3
PIP?=$(PYTHON) -m pip

docker-up:
	docker-compose up airflow-init
	docker-compose up -d

docker-down:
	docker-compose down --volumes --rmi all

clean: docker-down