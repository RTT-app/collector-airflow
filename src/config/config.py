import json

# read config json file
config = open('src/config/config.json', 'r+')
config_obj = json.load(config)

# tokens
CLIENT_ID = config_obj.get("client_id")
SECRET_TOKEN = config_obj.get("secret_token")
USER_AGENT = config_obj.get("user_agent")
SUBREDDIT = config_obj.get("subreddit")