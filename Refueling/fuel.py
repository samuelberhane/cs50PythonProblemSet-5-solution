def main():
    fraction = input("Fraction: ")
    f_convert = convert(fraction)
    result = gauge(f_convert)
    print(result)


def convert(fraction):
    while True:
        try:
            x,y = fraction.split('/')
            x_num = int(x)
            y_num = int(y)
            fuel_num = x_num / y_num
            if fuel_num <= 1:
                percentage = int(fuel_num * 100)
                return percentage
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError,ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()