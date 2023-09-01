import pendulum
import requests
from airflow.decorators import dag, task

@dag(
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["Reddit-ETL"],
)
def reddit_etl():
    @task()
    def extract():
        """
        #### Load task
        """
        extract_url = 'http://localhost:5000/extract'
        id_ = requests.post(extract_url)
        
        return id_

    @task()
    def load(id_):
        """
        #### Load task
        """
        transform_url = 'http://localhost:5000/transform'
        id_ = requests.put(transform_url)
        
        return id_

    @task()
    def load():
        """
        #### Load task
        """
        get_transformed_data_url = 'http://localhost:5000/get-transformed-data/<string:id>'
        load_url = 'http://localhost:5001/get-transformed-data/<string:id>'

        id_ = requests.get(transform_url)

    load()

etl_pipeline = reddit_etl()