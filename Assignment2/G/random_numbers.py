__author__ = "Tadj Cazaubon"

"""
This program reads a positive integer n from the keyboard and then:
- Generates and prints (in a single line) n random numbers in the interval [1,100]
- Prints the average value (with two decimals), the smallest number (min), and the largest number (max).
An example of an execution:
"""

"""randint method imported to generate random number"""
from random import randint

"""Number set to None type to be compared without throwing error."""
number = None


while type(number)!=int or number<0:
    try:
        number = input("\nEnter number of integers to be generated: ")
        number = int(number)
        
        if number<0:
            raise Exception

    except Exception:
        print("\n>>> ERROR: Input must be positive.")


"""Since we aren't allowed to store the numbers in a data structure before calculation as a rule, 
    we must do it on the fly during iteration right after generation."""

total = 0
current_max = 0
current_min = 100

generated = [ ]

for x in range(0,number):
    
    n = randint(1,100)
    """add the generated number to the running total"""
    total+=n

    """if the current maximum is less than the generated number, replace it with the number."""
    if current_max<n:
        current_max = n
    """If the current minimum is more than the number, replace it with the number"""
    if current_min>n:
        current_min = n
    
    """Append generated integer to list and join as string to make easier to print later"""
    generated.append(n)
    generated_str = ' '.join(str(a) for a in generated)

"""Average rounded to two decimals"""
average = round(total/number,1)

print(f"\n Genrated values: {generated_str} \n Average, min, and max are {average}, {current_min}, and {current_max} \n")