__author__ = "Tadj Cazaubon"

"""
Program will calculate the area of a circle given its radius as user input.
Revised 07/09/21
"""

#Closest real number representation of pi
pi = 355/113

radius = float(input("\n > Provide Radius: "))

#print area rounded off to single decimal
print(f"\n> Corresponding area is {round(pi*(radius**2),1)} \n")