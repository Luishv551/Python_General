import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r'^(\d{1,2}):(\d{2}) (AM|PM) to (\d{1,2}):(\d{2}) (AM|PM)$'

    match = re.match(pattern, s)

    if not match:
        raise ValueError("Invalid input format. Please provide time in format'9:00 AM to 5:00 PM' or '9 AM to 5 PM'.")

    start_hour = int(match.group(1))
    start_minute = int(match.group(2))
    start_meridiem = match.group(3)
    end_hour = int(match.group(4))
    end_minute = int(match.group(5))
    end_meridiem = match.group(6)

    if start_hour < 1 or start_hour > 12 or start_minute < 0 or start_minute > 59:
        raise ValueError("Invalid Start Time")
    if end_hour < 1 or end_hour > 12 or end_minute < 0 or end_minute > 59:
        raise ValueError("Invalid end time.")

    if start_meridiem == "PM" and start_hour != 12:
        start_hour += 12
    elif start_meridiem == "AM" and start_hour == 12:
        start_hour = 0

    if end_meridiem == "PM" and end_hour != 12:
        end_hour += 12
    elif end_meridiem == "AM" and end_hour == 12:
        end_hour = 0

    start_time_24hr = '{:02d}:{:02d}'.format(start_hour, start_minute)
    end_time_24hr = '{:02d}:{:02d}'.format(end_hour, end_minute)
    return f"{start_time_24hr} to {end_time_24hr}"

if __name__ == "__main__":
    main()
