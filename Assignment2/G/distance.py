__author__ = "Tadj Cazaubon"


from math import sqrt

def distance(x1,y1,x2,y2):

    distance = sqrt( (x1-x2)**2 + (y1-y2)**2 )
    distance = round(distance,3)

    print(f"\nThe distance between ({x1},{y1}) and ({x2},{y2}) is {distance} \n")


x1 = float(input("\nEnter x1: "))
x2 = float(input("\nEnter x2: "))
y1 = float(input("\nEnter y1: "))
y2 = float(input("\nEnter y2: "))

distance(x1,y1,x2,y2)