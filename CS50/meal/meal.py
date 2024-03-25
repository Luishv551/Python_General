def main():

    time_now = input("What time is it? ")

    hours = convert(time_now)

    if 7 <= hours <= 8:
        return "Breakfast time"
    elif 12 <= hours <= 13:
        return "Lunch time"
    elif 18 <= hours <= 19:
        return "Dinner time"

def convert(time):

    time = time.split(":")

    hours = float(time[0])
    minutes = float(time[1])

    minutes_convert = minutes / 60

    time_final = hours + minutes_convert

    return time_final

    return

if __name__ == "__main__":
    result = main()
    print(result)

