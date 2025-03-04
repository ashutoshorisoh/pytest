#In pytest, fixtures are a way to set up preconditions or provide reusable test dependencies before running a test function. They help in setting up test data, initializing objects, connecting to databases, etc.
#only fixture function cannot have test_ thing
#Yes, in a fixture function, you should NOT prefix the name with test_, otherwise it will run as a normal test.
#yeild is used for post condition
#actually in real world it is used as fixture function for url and data required and shit and yield is put and after that driver.close() kind of thing
import pytest


@pytest.fixture()
def setup():
    print("i will run first")
    yield
    print("i will run last")

def test_hey(setup):
    print("i will run second")

def setcheck():
    print("i will not run because i am not starting with test_ or marked as any fixture and thing")