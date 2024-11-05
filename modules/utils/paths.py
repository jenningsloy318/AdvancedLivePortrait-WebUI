import functools
import os


PROJECT_ROOT_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "..")
MODELS_DIR = os.path.join(PROJECT_ROOT_DIR, "models")


@functools.lru_cache
def init_dirs():
    for dir_path in [
        MODELS_DIR
    ]:
        os.makedirs(dir_path, exist_ok=True)


init_dirs()