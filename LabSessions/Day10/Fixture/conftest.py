import pytest

@pytest.fixture(scope="function")
def func_setup():
    print("\nfunction setup")
    yield
    print("\nfunction teardown")


@pytest.fixture(scope="class")
def class_setup():
    print("\nclass setup")
    yield
    print("\nclass teardown")


@pytest.fixture(scope="module")
def module_setup():
    print("\nmodule setup")
    yield
    print("\nmodule teardown")


@pytest.fixture(scope="session")
def session_setup():
    print("\nsession setup")
    yield
    print("\nsession teardown")
