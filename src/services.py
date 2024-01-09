import os as _os
import random as _random
from typing import List


def _get_image_files(directory_name: str) -> List[str]:
    return _os.listdir(directory_name)


def select_random_image(directory_name: str) -> str:
    images = _get_image_files(directory_name=directory_name)
    random_image = _random.choice(images)
    path = f"{directory_name}/{random_image}"
    return path
