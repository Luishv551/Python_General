def main():

    input_user = input("Input:")
    input_user = list(input_user)
    print(shorten(input_user))

def shorten(input_user):

    novogals_word = ""
    vogals = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

    for _ in input_user:
        if _ not in vogals:
            novogals_word += _
    return novogals_word


if __name__ == "__main__":
    main()
