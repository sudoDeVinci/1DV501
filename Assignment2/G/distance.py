__author__ = "Tadj Cazaubon"

"""
This program creates a function which computes the distance between two points (x1,y1) and (x2,y2) using :
distance = Sqrt( (x1-x2)^2 + (y1-y2)^2 )
    
The answer should be presented with three decimal digits.
"""


#Method imported to calculate square root
from math import sqrt


def distance(x1,y1,x2,y2):

    #Calculate distance
    distance = sqrt( (x1-x2)**2 + (y1-y2)**2 )
    #Round off distance to 3 digits
    distance = round(distance,3)
    
    return distance

#User inputs x and y points (Assumed to be correct input)
x1 = float(input("\nEnter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

#Assign function return to variable to print
dist = distance(x1,y1,x2,y2)

print(f"\nThe distance between ({x1},{y1}) and ({x2},{y2}) is {dist} \n")