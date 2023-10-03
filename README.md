# Airflow Pipeline Repository

This repository contains the source code for an Apache Airflow DAG (Directed Acyclic Graph) that manages a data pipeline. The Airflow DAG file, `dag_reddit.py`, defines the data pipeline tasks, dependencies, and scheduling. You can customize the DAG to fit your specific data processing needs. It also includes a `docker-compose.yml` file to easily set up an Apache Airflow environment for testing and development.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following requirements installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Make (to automate the project execution)
- Python 3.10 (also install pip to manage python modules)

To setup the Python environment, you should define ```.env``` file containing ```AIRFLOW_UID``` env var following the airflow [guide](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html). 

### Running Apache Airflow project

1. Clone this repository to your local machine:

```bash
$ git clone https://github.com/RTT-app/collector-airflow.git
$ cd collector-airflow
```

2. Run make command to up app container on machine:

Run the command below to up Docker container with airflow modules (to see more details about, access the airflow [documentation](https://airflow.apache.org/docs/apache-airflow/stable/index.html)) and schedule Reddit pipeline described in DAG file.

```bash 
$ make up
```
### Stop project app

Run the command below to clear all the files in the docker container from the application modules environment.

1. Run make command to stop containers and clean all files from the app:
```bash
$ make clean
```
