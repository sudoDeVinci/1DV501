__author__ = "Tadj Cazaubon"

from random import randint
from sys import exit

"""
Choose a random integer between 1-100, user guesses value.
After each guess, the user is given a clue of the type higher or lower.
"""


"""Give a random number between 1 and 100"""
answer = randint(1, 100)

"""Initiate the guess variable with None so it can be checked against answer"""
guess = None
"""Number of attempts user takes to correctly guess"""
attempts = 0

"""Program doesn't terminate unless guess matches generated answer"""
while guess != answer:

    """Exit program if 10 attempts are made"""
    if attempts == 10:
        print("You're obviously not taking this seriously.")
        exit(0)
    try:
        """iterate attempts"""
        attempts += 1
        guess = input("Enter a guess: ")

        """attempt to convert input to int, otherwise, raise error"""
        guess = int(guess)
    except Exception:
        print("Guess must be an int")

    while type(guess) != int:

        try:
            """attempt to convert input to int, otherwise, raise error"""
            guess = int(input("\nEnter a guess: "))
        except Exception:
            print("Guess must be an int")

    if guess > answer:
        print("  Clue: Lower")
    elif guess < answer:
        print("  Clue: Higher")
print(f"\n  Correct answer after {attempts} guesses!\n")
