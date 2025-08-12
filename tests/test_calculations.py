from app.calculations import add, subtract,multiply, devide


def test_add():
    print("Testing add function")
    assert add(5, 3) == 8
    
def test_subtract():
    assert subtract(9, 4) == 5
    
def test_multiply():
    assert multiply(2, 3) == 6
    
def test_devide():
    assert devide(8, 4) == 2
    
