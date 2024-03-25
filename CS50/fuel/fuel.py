def fuel_percentage():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = map(int, fraction.split('/'))

            if x < 0 or y <= 0 or x > y:
                fraction = input("Fraction: ")
                x, y = map(int, fraction.split('/'))

            x = int(x)
            y = int(y)

            percent = (x / y) * 100

            percent = round(percent)

            percent = int(percent)

            if percent <= 1:
                print('E')
                break
            elif percent >= 99:
                print('F')
                break
            else:
                print (f'{percent}%')
                break

        except (ValueError, ZeroDivisionError):
            pass

fuel_percentage()
