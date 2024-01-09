import os as _os
import random as _random
import time as _time
import fastapi as _fastapi
from typing import List


def _get_image_files(directory_name: str) -> List[str]:
    return _os.listdir(directory_name)


def select_random_image(directory_name: str) -> str:
    """
    Produces a path of a random Image from a selected directory.
    """
    images = _get_image_files(directory_name=directory_name)
    random_image = _random.choice(images)
    path = f"{directory_name}/{random_image}"
    return path


def _is_image(filename: str) -> bool:
    """
    Makes sure that the file is only image, nothing else.
    """
    valid_extensions = (".png", ".jpg", ".jpeg", ".gif")
    return filename.endswith(valid_extensions)


def upload_images(directory_name: str, image: _fastapi.UploadFile):
    if _is_image(image.filename):
        time_string = _time.strftime("%Y%M%d-%H%M%S")
        image_name = time_string + image.filename.replace(" ", "-")

        with open(f"{directory_name}/{image_name}", 'wb+') as image_upload:
            image_upload.write(image.file.read())

        return f"{directory_name}/{image_name}"
    
    return None
