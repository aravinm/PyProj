from contextlib import contextmanager

@contextmanager
def ignored(*exceptions):
    """ignore exceptions, implement suppress from python 3.4"""
    try:
        yield
    except exceptions:
        pass