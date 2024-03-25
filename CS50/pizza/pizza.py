import sys
import csv
from tabulate import tabulate

def print_table(csv_file):
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = list(reader)
    print(tabulate(rows, headers=headers, tablefmt='grid'))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")

    csv_file = sys.argv[1]

    if not csv_file.endswith('.csv'):
        sys.exit("Not a CSV file")

    try:
        print_table(csv_file)
    except FileNotFoundError:
        sys.exit("File does not exist")
