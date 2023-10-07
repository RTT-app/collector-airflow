import pendulum
import requests
from airflow.decorators import dag, task
from datetime import datetime 

@dag(start_date=datetime(2023,10,7), 
     schedule='@hourly',
     catchup=False, 
     tags=["Reddit-ETL"],
     is_paused_upon_creation=False
     )
def reddit_etl():
    @task()
    def extract():
        """
        #### Load task
        """
        extract_url = 'http://172.20.0.7:5000/extract'
        response = requests.post(extract_url)
        id_ = response.json()['id']
        
        return id_
    

    @task()
    def transfrom(id):
        """
        #### Load task
        """
        extract_url = f'http://172.20.0.7:5000/transform/{id}'
        response = requests.get(extract_url)
        posts = response.json()
        
        return posts


    @task()
    def load(posts):
        load_url = 'http://172.19.0.5:5001/add-post'
        
        for post in range(len(posts['posts']['comment'])):
            comment = {
                       "comment": posts['posts']['comment'][post],
                       "score": posts['posts']['score'][post],
                       "self_text": posts['posts']['self_text'][post],
                       "title": posts['posts']['title'][post]
                       }
            requests.post(load_url, json=comment)
    
    id_ = extract()
    data = transfrom(id_)
    load(data)

etl_pipeline = reddit_etl()
