from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import os

dotenv_path = find_dotenv(filename='.env')

if not Path(dotenv_path).exists():
    os.system("touch .env")

load_dotenv(dotenv_path)

# Reddit praw client config vars
CLIENT_ID = os.getenv('CLIENT_ID')
SECRET_TOKEN = os.getenv('SECRET_TOKEN')
USER_AGENT = os.getenv('USER_AGENT')
SUBREDDIT = os.getenv('SUBREDDIT')
N_POSTS = os.getenv('N_POSTS')

# DB api config vars
API_IP = os.getenv('API_IP')
API_PORT = os.getenv('API_PORT')

# DB api endpoints
REGISTER_POST = f'http://{API_IP}:{API_PORT}/add-post'

