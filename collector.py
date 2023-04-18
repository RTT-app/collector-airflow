import praw
import time
import pandas as pd
from utils import update_search 
from config import (
    CLIENT_ID, 
    SECRET_TOKEN,
    USER_AGENT,
    SUBREDDIT
)

# create a Reddit instance using the praw library and your API credentials
reddit = praw.Reddit(
        client_id= CLIENT_ID,
        client_secret= SECRET_TOKEN,
        user_agent= USER_AGENT
        )

# specify the subreddit you want to retrieve posts from
subreddit = reddit.subreddit(SUBREDDIT)

# retrieve the top 10 hot posts from the subreddit
top_posts = subreddit.new(limit=10) # jogar isso pra dentro do while

# data
data = {
        "title":[],
        "self_text":[],
        "comment":[]
        }
"""
        "upvote":[],
        "downvote":[],
        "like":[],
        "score":[]
        }
"""

# loop through each post and print its title and score
minutos = 1
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

#print(data)
data = pd.DataFrame.from_dict(data)
data.to_csv('exp.csv')