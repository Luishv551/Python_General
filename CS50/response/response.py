import validators

def main():
    email = input("Please enter your email address: ")
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
