import os


def file_path(filename):
    return f"{os.environ.get('IMAGE_DIRECTORY')}/{filename}"
