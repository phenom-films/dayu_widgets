import os

STATIC_PATH = __path__[0]


def request_file(name):
    return os.path.join(STATIC_PATH, name)
