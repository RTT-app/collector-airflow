from modules.collector import Collector
from config.config import (
    CLIENT_ID, 
    SECRET_TOKEN,
    USER_AGENT,
    SUBREDDIT
)

class RedditCollector():

    def run(self):
        collector = Collector(CLIENT_ID, SECRET_TOKEN, USER_AGENT, SUBREDDIT)
        collector.run()

if __name__ == "__main__":
    lyric = RedditCollector()
    lyric.run()