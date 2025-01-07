import pytest

def method1():
    print("Hello World")

@pytest.mark.smoke
def test_method2():
    print("test1")
    assert 1-1 == 2

@pytest.mark.regression
def test_method3():
    print("test2")
    assert 1 + 1 == 2

@pytest.mark.regression
def test_method4():
    print("test3")
    assert 1 + 1 != 3