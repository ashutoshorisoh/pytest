import pytest


@pytest.fixture(scope='class')
def setup():
    print("setting up")
    yield
    print("tearing down")

@pytest.fixture(scope='class')
def dataDrivenFixture():
    return ("hey","1","am","here")

import pytest

import pytest

# ✅ This fixture will run **2 times** because we have **2 dictionaries** inside the list.
@pytest.fixture(params=[{"a": 1}, {"b": 2}])
def parameter(request):
    # `request.param` will first be {"a": 1}, then {"b": 2}
    # `request.param.values()` gives dict_values([1]) for {"a": 1} and dict_values([2]) for {"b": 2}
    # Converting to list -> list(request.param.values()) gives [1] and [2]
    # Using [0] -> Extracts only the **first and only value** from the dictionary (1, then 2)
    return list(request.param.values())[0]

# ✅ Test function runs **2 times**, once with **1**, then with **2**


