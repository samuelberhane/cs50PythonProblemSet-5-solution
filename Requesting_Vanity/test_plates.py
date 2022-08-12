from plates import is_valid

def main():
    test_valid1()
    test_valid2()
    test_valid3()
    test_valid4()
    test_valid5()
    test_valid6()
    test_valid7()

def test_valid1():
    assert is_valid("CS50") == True

def test_valid2():
    assert is_valid("CS05") == False

def test_valid3():
    assert is_valid("CS50P") == False

def test_valid4():
    assert is_valid("PI3.14") == False

def test_valid5():
    assert is_valid("H") == False

def test_valid6():
    assert is_valid("OUTATIME") == False

def test_valid7():
    assert is_valid("12TATIME") == False


if __name__ == "__main__":
    main()