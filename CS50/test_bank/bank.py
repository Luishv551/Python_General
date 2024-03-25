def main():
    ask = input("Greeting: ")
    print(f"${value(ask)}")

def value(greeting):
    word = greeting.lower().strip()
    if "hello" in word:
        return int(0)
    elif word[0] == "h":
        return int(20)
    else:
        return int(100)


if __name__ == "__main__":
    main()
