__author__ = "Tadj Cazaubon"

"""
Program will find the celsius equivalent to
a user provided temperature in fahrenheit
Revised 07/09/21
"""

fahrenheit = input("\n>Enter temp in farenheit: ")

# if input cannot be converted to float, request different input
try:
    float(fahrenheit)

except Exception:

    # isinstance checks if a variable is specified datatype
    while isinstance(fahrenheit, float) is False:
        fahrenheit = input("\n>Enter temp in farenheit [Must be float]: ")
        try:
            float(fahrenheit)
            break
        except Exception:
            continue

# Calculate celsius equivalent
celsius = 5*(float(fahrenheit)-32)/9

print(f"\n> Corresponding temperature in Celsius is: {celsius} ")
