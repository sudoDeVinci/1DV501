__author__ = "Tadj Cazaubon"

"""
This program finds four integers, A, B, C and D, such that
the number DCBA is equal to 4 times the number ABCD, given that:
    + neither A nor D can be 0
    + ABCD and DCBA are proper 4 digit integers

Since the range is 1001 to 9999, then ABCD can have a maximum value of
roughly 2500
"""
possible_abcd = range(1001, 2500)

for digit in possible_abcd:
    # Multiply the digit by four
    fourX = str(4*digit)
    digit = str(digit)
    # Reverse digit to get possible DCBA"
    possible_dcba = digit[::-1]

    if fourX == possible_dcba:
        # Assign each digit from DCBA
        D, C, B, A = possible_dcba
        print(f"A: {A}, B:{B}, C:{C}, D:{D}")
        break
