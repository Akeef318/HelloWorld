import random


def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)


def main():
    min_value = int(input(1))
    max_value = int(input(10))

    if min_value > max_value:
        print("Minimum value cannot be greater than maximum value.")
        return

    random_number = generate_random_number(1, 10)

    guess = int(input(f"Guess the number between {1} and {10}: "))

    if guess == random_number:
        print("Congratulations! Your guess is correct.")
    else:
        print(f"Sorry, the correct number was {random_number}. Better luck next time!")


if __name__ == "__main__:":
    main()