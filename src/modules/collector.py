import os
import time
import praw
import pandas as pd
from src.utils import update_search 

class Collector():

    def __init__(self, client_id, secret_token, user_agent, subreddit_name):
    
        # create a Reddit instance using the praw library and your API credentials
        self.client = praw.Reddit(
                client_id= client_id,
                client_secret= secret_token,
                user_agent= user_agent
                )

        # specify the subreddit you want to retrieve posts from
        self.subreddit_ = self.client.subreddit(subreddit_name)

    def get_data(self, post_amount, experiment_time):
        # retrieve the top 10 hot posts from the subreddit
        top_posts = self.subreddit_.new(limit=post_amount) # jogar isso pra dentro do while

        data = {
                "title":[],
                "self_text":[],
                "comment":[]
                }

        # loop through each post and print its title and score
        minutos = experiment_time
        up = True
        past = time.time()

        while up:
            for post in top_posts:
                for comment in post.comments:
                    try:
                        exists = update_search(data["comment"], comment.body) 
                        if not exists:
                            data["title"].append(post.title)
                            data["self_text"].append(post.selftext)
                            data["comment"].append(comment.body)
                    except AttributeError:
                        pass
            
            actual = time.time() - past
            if actual >= (minutos * 60):
                up = False
        self.data = data
    
    def save_data(self):
        os.system("mkdir ../data")
        data = pd.DataFrame.from_dict(self.data)
        data.to_csv('../data/exp.csv')