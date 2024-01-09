import os as _os
import dotenv as _dotenv
import praw as _praw

_dotenv.load_dotenv()

def create_reddit_client():
    client = _praw.Reddit(
        client_id=_os.environ["CLIENT_ID"],
        client_secret=_os.environ["CLIENT_SECRET"],
        user_agent=_os.environ["USER_AGENT"]
    )
    return client
