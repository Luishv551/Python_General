def main():
    fraction = input("Fraction: ")
    print(gauge(convert(fraction)))


def convert(fraction):
    try:
        x, y = map(int, fraction.split('/'))

        if y == 0:
            raise ZeroDivisionError
        if x < 0 or y <= 0 or x > y:
            raise ValueError

        percentage = (x / y) * 100
        percentage = round(percentage)

    except ValueError:
        raise
    except ZeroDivisionError:
        raise ZeroDivisionError

    return int(percentage)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
