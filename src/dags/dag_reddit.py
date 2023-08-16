import json
import pendulum
import praw
import requests
from airflow.decorators import dag, task
from config import (
                    CLIENT_ID, 
                    SECRET_TOKEN, 
                    USER_AGENT, 
                    SUBREDDIT,
                    REGISTER_POST,
                    N_POSTS
                    )
from modules.untils import (
                            stemm_comments, 
                            clean_text
                            )

@dag(
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["Reddit-ETL"],
)
def reddit_etl():
    """
    ### TaskFlow API Tutorial Documentation
    This is a simple data pipeline example which demonstrates the use of
    the TaskFlow API using three simple tasks for Extract, Transform, and Load.
    Documentation that goes along with the Airflow TaskFlow API tutorial is
    located
    [here](https://airflow.apache.org/docs/apache-airflow/stable/tutorial_taskflow_api.html)
    """
    @task()
    def extract():
        """
        #### Extract task
        A simple Extract task to get data ready for the rest of the data
        pipeline. In this case, getting data is simulated by reading from a
        hardcoded JSON string.
        """
        client = praw.Reddit(
                client_id= CLIENT_ID,
                client_secret= SECRET_TOKEN,
                user_agent= USER_AGENT
                )
        
        subreddit = client.subreddit(SUBREDDIT)

        top_posts = subreddit.new(limit=N_POSTS) # jogar isso pra dentro do while

        data = {
                "title":[],
                "self_text":[],
                "comment":[],
                "score":[]
                }

        for post in top_posts:
                for comment in post.comments:
                        data["title"].append(post.title)
                        data["self_text"].append(post.selftext)
                        data["comment"].append(comment.body)
                        data["score"].append(comment.score)

        return data
    

    @task(multiple_outputs=True)
    def transform(data: dict):
        """
        #### Transform task
        A simple Transform task which takes in the collection of order data and
        computes the total order value.
        """
        data["self_text"] = clean_text(data["self_text"])
        data["self_text"] = stemm_comments(data["self_text"])

        data["comment"] = clean_text(data["comment"])
        data["comment"] = stemm_comments(data["comment"])
        
        return data
    
    
    @task()
    def load(clean_comments: dict):
        """
        #### Load task
        A simple Load task which takes in the result of the Transform task and
        instead of saving it to end user review, just prints it out.
        """
        print('saved_data')


    raw_comments = extract()
    clean_comments = transform(raw_comments)
    load(clean_comments)

etl_pipeline = reddit_etl()