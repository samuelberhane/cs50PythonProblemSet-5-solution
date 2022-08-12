from twttr import shorten

def main():
    test_shorten_small()

def test_small():
    assert shorten("samuel") == "sml"
def test_capital():
    assert shorten("NAME") == "NM"
def test_number():
    assert shorten("1234") == "1234"
def test_punctuation():
    assert shorten(";!@") == ";!@"


if __name__ == "__main__":
    main()