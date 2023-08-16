import requests
from config import REGISTER_POST

def add_post(post: dict) -> bool:
    r = requests.post(REGISTER_POST, data=post)
    
    if r.status_code == 200:
        return True
    
    return False