import os as _os
import random as _random
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
