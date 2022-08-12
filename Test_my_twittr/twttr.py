def main():
    word_input = input('Input: ')
    result = shorten(word_input)
    print("Output:",result)


def shorten(word):
    final_word = ''
    for char in word:
        if char.lower() not in "aeiou":
            final_word += char
    return final_word

if __name__ == "__main__":
    main()
