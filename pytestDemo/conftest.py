import pytest


@pytest.fixture(scope='class')
def setup():
    print("setting up")
    yield
    print("tearing down")

@pytest.fixture(scope='class')
def dataDrivenFixture():
    return ("hey","1","am","here")

