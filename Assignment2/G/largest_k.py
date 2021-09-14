__author__ = "Tadj Cazaubon"

"""
This program takes a positive integer as user input, and computes 
the largest integer k, such that 0+2+4+6+8+...+k<n.
"""

"""module method needed to exit during errors""" 
from sys import exit

"""Take input from user"""
input_int = input("\nEnter a positive integer: ")

try:
    """Try to convert string input to integer, 
        if cannot, will raise a ValueError"""
    input_int = int(input_int)

    """Check if integer is positive, else 
        raise an arbitrary error"""
    if input_int<=0:       
        raise Exception


except ValueError:
    """exit message for raising error"""
    print("\nInput provided is not an integer")

    """Program exits with error"""
    exit(1)

except Exception:
    """exit message for raising error"""
    print("\nInteger provided is not positive")

    """Program exits with error"""
    exit(1)

"""Tracker for cummulative total"""
cumm = 0




sequence = range(0,input_int,2)

for even_int in sequence:
    if input_int - (cumm+even_int) > 0:
        k = even_int
        cumm+=even_int
        #print(f"number:{even_int}, cumm:{cumm}\n")
        

print(f"\n{k} is the largest k such that 0+2+4+6+...+k < {input_int} \n")