__author__ = "Tadj Cazaubon"

"""
This program reads a positive integer n from the keyboard and then:
- Generates and prints (in a single line) n random numbers in the interval [1,100]
- Prints the average value (with two decimals), the smallest number (min), and the largest number (max).
An example of an execution:
"""

from random import randint

number = None


while type(number)!=int or number<0:
    try:
        number = input("\nEnter number of integers to be generated: ")
        number = int(number)
        
        if number<0:
            raise Exception

    except Exception:
        print("\n>>> ERROR: Input must be positive.")


generated = [randint(1,100) for x in range(0,number)]

print(f"\nGenerated Values: {generated}")

average = sum(generated)/len(generated)
maximum = max(generated)
minimum = min(generated)

print(f"\nAverage, Max and Min: {average}, {maximum}, {minimum} \n")

