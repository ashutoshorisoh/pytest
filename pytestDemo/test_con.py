import pytest


def test_first(setup):
    print('i wil run after setup')

@pytest.mark.usefixtures("setup")
class TestCheck:
    def test_oneCheck(self):
        print("one after setup")

    def test_twoCheck(self):
        print("two after setup")

