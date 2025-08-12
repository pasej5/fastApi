import pytest
from app.calculations import add, subtract,multiply, devide


@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 8),
    (10, 5, 15),
    (12, 4, 16)
])
def test_add(num1, num2, expected):
    print("Testing add function")
    assert add(num1, num2) == expected
    
def test_subtract():
    assert subtract(9, 4) == 5
    
def test_multiply():
    assert multiply(2, 3) == 6
    
def test_devide():
    assert devide(8, 4) == 2
    
