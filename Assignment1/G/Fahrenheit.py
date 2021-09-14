__author__ = "Tadj Cazaubon"

"""
Program will find the celsius equivalent to a user provided temperature in fahrenheit.
Revised 07/09/21
"""

fahrenheit = input("\n>Enter temp in farenheit: ")

#if input cannot be converted to float, request different input
try:
    float(fahrenheit)

except Exception:

    #isinstance checks if a variable is of a specified datatype 
    while isinstance(fahrenheit,float)==False:
        fahrenheit = input("\n>Enter temp in farenheit [Must be floating point]: ")
        try:
            float(fahrenheit)
            break
        except:
            continue

#Calculate celsius equivalent
celsius = 5*(float(fahrenheit)-32)/9

print(f"\n> Corresponding temperature in Celsius is: {celsius} ")

print("_")