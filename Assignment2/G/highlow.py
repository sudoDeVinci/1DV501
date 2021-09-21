__author__ = "Tadj Cazaubon"

"""
Implementation for the game High and Low. The computer chooses a random integer between 1 and 100 and lets the user guess the value.
After each guess, the user is given a clue of the type higher or lower.
"""


"""Module methods needed to create random number, and exit program with an error"""
from random import randint
from sys import exit

"""Give a random number between 1 and 100"""
answer = randint(1,100)
"""Initiate the guess variable with None value so it can be checked against answer"""
guess = None
"""Number of attempts user takes to correctly guess"""
attempts = 0

"""Program doesn't terminate unless guess matches generated answer"""
while guess != answer:

    """Exit program if 10 attempts are made"""
    if attempts ==10:
        print("\nYou're obviously not taking this seriously.")
        exit(0)
    try:
        """iterate attempts"""
        attempts+=1
        
        guess = input("\nEnter a guess: ")

        """attempt to convert input to int, otherwise, raise error"""
        guess = int(guess)
    except:
        print("\nGuess must be an int")


    while type(guess) != int:

        try:
            """attempt to convert input to int, otherwise, raise error"""
            guess = int(input("\nEnter a guess: "))
        except:
            print("\nGuess must be an int")


    if guess>answer:
        print("\n> Lower")

    elif guess<answer:
        print("\n> Higher")
    
print(f"\nYou got it! \nYour guess: {guess} \nAnswer: {answer} \nAttempts: {attempts} \n")

    
