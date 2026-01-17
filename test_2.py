from air import arithmetic_operations

def test_positive_numbers():
    assert arithmetic_operations(10, 5) == (15, 5, 50, 2.0)

def test_with_zero():
    assert arithmetic_operations(5, 1) == (6, 4, 5, 5.0)

def test_negative_numbers():
    assert arithmetic_operations(-10, -5) == (-15, -5, 50, 2.0)
