from bank import value

def main():
    test_value1()
    test_value1()
    test_value1()
    test_value4()

def test_value1():
    assert value("HELLO") == 0
def test_value2():
    assert value('h') == 20
def test_value3():
    assert value("100") == 100
def test_value4():
    assert value("how are you doing?") == 20

if __name__ == "__main__":
    main()