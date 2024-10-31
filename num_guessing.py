# Program to guess the number between 1-4

import random

secret_num = random.randint(1, 4)

print("Welcome to the Number Guessing Game!")

while True:
    try:
        guess = int(input("Enter the number between (1-4): "))

        if guess < 1 or guess > 4:
            print("Guess a number between 1 - 4!")
            continue

        if guess == secret_num:
            print(f"Congratulations! You have guessed the number {secret_num}!")
            break
        else:
            print("Incorrect guess. Try again!")

    except ValueError:
        print("Invalid input!")
