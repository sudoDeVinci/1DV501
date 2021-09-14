__author__ = "Tadj Cazaubon"

from random import randint

"""
Program generates a random number in the interval [-10,10] and classifies it as odd/even and as positive/negative.
Revised 07/09/21
"""

#random integer calculated
generated = randint(-10,11)

#special case made if generated digit is 0
if generated == 0:
    oddOrEven = "even"
    posOrNeg = "neither positive nor negative"

else:
    #Check if digit is odd or even
    if (generated % 2) == 0:
        oddOrEven = "even"
    else:
        oddOrEven = "odd"

    #Check if digit is positive or negative
    if (generated>0):
        posOrNeg = "positive"
    else:
        posOrNeg = "negative"

#Print given digit
print(f"\n> The generated number is {generated}")

#print result 
print(f"\n{generated} is {oddOrEven} and {posOrNeg}\n")