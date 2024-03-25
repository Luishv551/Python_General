import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # Using regular expression to find occurrences of "um" as a whole word
    um_count = len(re.findall(r'\bum\b', s, flags=re.IGNORECASE))
    return um_count

if __name__ == "__main__":
    main()
