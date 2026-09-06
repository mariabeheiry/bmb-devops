from app import add_numbers, subtract_numbers, multiply_numbers

def test_add_numbers():
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_subtract_numbers():
    assert subtract_numbers(3, 2) == 1
    assert subtract_numbers(2, 3) == -1
    assert subtract_numbers(0, 0) == 0

def test_multiply_numbers():
    assert multiply_numbers(3, 2) == 6
    assert multiply_numbers(-1, 1) == -1
    assert multiply_numbers(0, 5) == 0