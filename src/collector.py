import os as _os
import dotenv as _dotenv
import praw as _praw
import urllib.parse as _parse
import requests as _requests

_dotenv.load_dotenv()


def _create_reddit_client():
    client = _praw.Reddit(
        client_id=_os.environ["CLIENT_ID"],
        client_secret=_os.environ["CLIENT_SECRET"],
        user_agent=_os.environ["USER_AGENT"]
    )
    return client


def _is_image(post):
    """
    Checks if the Reddit post is an Image.
    """
    try:
        return post.post_hint == "image"
    except AttributeError:
        return False


def _get_image_urls(client: _praw.Reddit, subreddit_name: str, limit: int):
    hot_memes = client.subreddit(subreddit_name).hot(limit=limit)
    image_urls = list()
    for post in hot_memes:
        if _is_image(post=post):
            image_urls.append(post.url)
        
    return image_urls


def _get_image_name(image_url: str) -> str:
    image_name = _parse.urlparse(image_url)
    return _os.path.basename(image_name)


def _create_folder(folder_name: str):
    """
    If the folder does not exist, then the function creates
    a folder using the given name. 
    """
    try:
        _os.mkdir(folder_name)
    except OSError:
        print("OOPS; Something went wrong !!")
    else:
        print("Folder created")


def _download_image(folder_name: str, raw_response, image_name: str):
    pass


# def _collect_memes(subreddit_name: str, limit: int=20):
#     """
#     Collect the images from the URLs and stores them into
#     the folders, named after their subreddits
#     """
#     client = _create_reddit_client()
#     image_urls = _get_image_urls(
#         client=client,
#         subreddit_name=subreddit_name,
#         limit=limit
#     )

#     for image_url in image_urls:
#         image_name = _get_image_name(image_url=image_url)
#         response = _requests.get(image_url, stream=True)

#         if response.status_code == 200:
#             response.raw.decode_content = True
#             _download_image()




if __name__ == '__main__':
    client = _create_reddit_client()
    urls = _get_image_url(client=client, subreddit_name="memes", limit=10)
    print(urls)
