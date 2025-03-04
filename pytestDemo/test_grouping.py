#we mark certain function as smoke and to run only those function command in cmd used is ">py.test -m smoke -v -s"
#same way for other markings too
#what is smoke testing?
#In pytest, you can mark some test functions as smoke to indicate that they belong to the smoke test suite. These tests typically cover:
#Basic functionality
#Core workflows
#Key integration points
#You can mark smoke tests using @pytest.mark.smoke

#to skip we use @pytest.mark.skip, this is inbuilt markings and skips the test csase which are marked as such
#smoke is a custom marking

#@pytest.mark.xfail #incase we want a test case to run but not report it because we know its a big then we use Xfail
#op:  3 passed, 1 skipped, 1 xfailed (it ran but no report)

import pytest


@pytest.mark.smoke
def test_checkLogin():
    print("checked")

@pytest.mark.skip
def test_checkSkip():
    print("skipped")

@pytest.mark.xfail #incase we want a test case to run but not report it because we know its a big then we use Xfail
def test_failingbutnotreported():
    a=3
    assert a==1, "test case failed"

def test_usinga():
    a=1
    print(a)
