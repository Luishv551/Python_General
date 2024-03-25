months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input('Date: ')
    try:
        # Check if the date is in the format MM/DD/YYYY
        month, day, year = date.split("/")
        if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
            break
    except ValueError:
        try:
            # Check if the date is in the format Month Day, Year
            month_str, day_str, year = date.split(" ")
            month = months.index(month_str) + 1

            if not day_str.endswith(","):
                continue

            day = day_str.replace(",", "")
            if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                break
        except (ValueError, IndexError):
            print()
            pass
year = year.strip()
print(f'{year}-{int(month):02}-{int(day):02}')

