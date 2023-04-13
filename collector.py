import praw
from config import (
    CLIENT_ID, 
    SECRET_TOKEN,
    USER_AGENT
)

# create a Reddit instance using the praw library and your API credentials
reddit = praw.Reddit(
        client_id= CLIENT_ID,
        client_secret= SECRET_TOKEN,
        user_agent= USER_AGENT
        )

# specify the subreddit you want to retrieve posts from
subreddit_name = 'politics'
subreddit = reddit.subreddit(subreddit_name)

# retrieve the top 10 hot posts from the subreddit
top_posts = subreddit.new(limit=1)
#print(type(list(top_posts)[0]))

# loop through each post and print its title and score
for post in top_posts:
    print(f"Title: {post.title}")
    print()
    print("Comments:")
    for comment in post.comments:
        print("     "+comment.body)
        print()
    
