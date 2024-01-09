import os as _os
import dotenv as _dotenv
import praw as _praw

_dotenv.load_dotenv()

def _create_reddit_client():
    client = _praw.Reddit(
        client_id=_os.environ["CLIENT_ID"],
        client_secret=_os.environ["CLIENT_SECRET"],
        user_agent=_os.environ["USER_AGENT"]
    )
    return client


def _get_image_url(client: _praw.Reddit, subreddit_name: str, limit: int):
    hot_memes = client.subreddit(subreddit_name).hot(limit=limit)
    image_urls = list()
    for post in hot_memes:
        image_urls.append(post.url)
    
    return image_urls


if __name__ == '__main__':
    client = _create_reddit_client()
    urls = _get_image_url(client=client, subreddit_name="memes", limit=10)
    print(urls)
