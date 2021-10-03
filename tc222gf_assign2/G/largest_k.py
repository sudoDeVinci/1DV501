__author__ = "Tadj Cazaubon"

from sys import exit

"""
This program takes a positive integer as user input, computes
the largest integer k, such that 0+2+4+6+8+...+k<n.
"""

try:
    """Take input from user"""
    input_int = input("\nEnter a positive integer: ")

    """ if input is not a digit raise an Exception"""
    if input_int.isdigit() is False:
        raise Exception

    input_int = int(input_int)
    """Check if integer is positive, else
        raise an exception"""
    if input_int <= 0:
        raise Exception

except Exception:
    """exit message for raising error"""
    print("\nInput is either non-integer or negative")

    """Program exits with error"""
    exit(1)

"""Tracker for cummulative total"""
cumm = 0

"""Create sequence from 0 taking steps of 2 up til our input integer"""
sequence = range(0, input_int, 2)

for even_int in sequence:
    """
    For each n in the sequence, (n+2)+cumm is done to see if it is more than
    the input integer, i. If it's less than i, then n+4 is checked, n+6, n+8,
    until a digit k, such that (n+2)+(n+4)+(n+6)+(n+8)+...+k<i. Once the sum
    of the numbers is greater than i, then that n = k and is the last number
    in the sequence and we stop iteration.
    """
    if input_int - (cumm + even_int) > 0:
        k = even_int
        cumm += even_int
        # print(f"number:{even_int}, cumm:{cumm}\n")

print(f"\n{k} is the largest k such that 0+2+4+6+...+k < {input_int} \n")
