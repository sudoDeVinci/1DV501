__author__ = "Tadj Cazaubon"

#Actual value of pi to compare against later
from math import pi
#Method to generate rando floating points numbers 
from random import uniform


"""
This program calculates an approxiamtion of pi, viaa the method below:

Assume a unit circle centred around origin inside a square with sides 2 like in the figure above. 
Assume also that we randomly generate N points (x,y) where both x and y are within the range [- 1,1]. 
The proportion of points inside the circle should then approximately be the same as the ratio between 
the circle area pi*R*R (which equals pi since R=1) and the square area 4. This relation can be used to 
compute an approximation of pi.

This program houses a function and its calls using  N=100, N=10000, and N=1000000 to return approximations
to pi for each, along with the delta between actual pi and the approxiamted value.
"""

#Since we are using this to check for mulitple values of N, it is best to create a function to reuse.
def pi_approximator(N):
    
    #list comprehension to get N number of floating values tuples in the form (x,y)
    points = [(uniform(-1.0,1.0),uniform(-1.0,1.0)) for (x,y) in zip(range(N),range(N))]

    #A counter of all the generated values which fall inside our given cirlce
    p_in_circ = 0


    """
    The general equation of a circle with radius R, and centre (h,k) is (x-h)^2 + (y-k)^2 < R^2
    Our unit circle has centre (0,0) and R = 1, so our equation => (x^2)+(y^2) < 1
    """
    for x,y in points:
        circ_eqn_check = (x**2)+(y**2)

        if circ_eqn_check<=1:
            p_in_circ+=1

    #Our approximation of pi is the proportion of the points within the circle multipled by 4
    pi_approx = (p_in_circ/N)*4
    print(f"\n{p_in_circ} out of {N} points are inside our circle\nApproximate pi: {pi_approx}\nDelta to pi: {abs(pi-pi_approx)} \n\n")

#Our function calls for multiple values opf N
pi_approximator(100)
pi_approximator(10000)
pi_approximator(1000000)