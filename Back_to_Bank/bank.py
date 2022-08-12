def main():
    greeting = input('Greeting: ')
    result = value(greeting)
    print(f"${result}")

def value(greeting):
    string = greeting.lower().strip()
    if 'hello' in string:
        return 0
    elif string[0] == 'h':
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()