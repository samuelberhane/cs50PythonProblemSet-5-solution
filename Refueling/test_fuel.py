import pytest
from fuel import convert, gauge

def main():
    test_all1()
    test_all2()
    test_gauge1()
    test_gauge2()
    test_zero_division()
    test_value_error()

def test_all1():
    assert convert("3/4") == 75 and gauge(75) == f"{75}%"

def test_all2():
    assert convert("1/4") == 25 and gauge(25) == f"{25}%"

def test_gauge1():
    assert convert("1/100") == 1 and gauge(1) == f"E"

def test_gauge2():
    assert convert("99/100") == 99 and gauge(99) == f"F"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")

if __name__ == "__main__":
    main()