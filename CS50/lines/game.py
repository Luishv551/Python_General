import random

def get_input(prompt, validation_func):
    while True:
        try:
            user_input = int(input(prompt))
            if validation_func(user_input):
                return user_input
        except ValueError:
            pass

def is_positive_integer_level(value):
    return value > 0

def is_positive_integer(value):
    return value >= 0

def main():
    # Prompt the user for a level
    level = get_input("level: ", is_positive_integer_level)

    # Randomly generate an integer between 1 and the level (inclusive)
    target_number = random.randint(1, level)

    while True:
        # Prompt the user to guess the integer
        user_guess = get_input("Guess: ", is_positive_integer)

        # Compare the guess with the target number
        if user_guess < target_number:
            print("Too small!")
        elif user_guess > target_number:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
