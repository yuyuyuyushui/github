import pytest

@pytest.fixture(scope="module",autouse=True)
def foo():
    print("fool")
    return 1