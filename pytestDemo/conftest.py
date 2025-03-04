import pytest


@pytest.fixture(scope='class')
def setup():
    print("setting up")
    yield
    print("tearing down")