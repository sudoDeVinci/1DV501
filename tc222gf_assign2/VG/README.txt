This file is a short list and description of the solutions to each VG python script
for Assignment 2.

+ birthday_candles.py: 

    <-> This program computes how many boxes of candles a person needs to buy each year for her\his birthday cake given the following:
        --> Each box contains 24 candles
        -->  The number of candles used each year is the same as the age
        --> You save non-used candles from one year to another
        --> The person reaches an age of 100

    <-> Firstly some simple counters are needed, like the number of candles left and the total number of boxes.
        each year we check if the number of candles left is less than what is needed that year. If less, then we buy a new box, adding
        24 to the number of candles left, and 1 to the total number of boxes and the number of boxes that year. This is within a while 
        loop which breaks when the number of candles is the same as the number needed that year. Once done, we subtract the number of 
        candles used from the number of candles left. If we had the buy any b oxes that year, we print the year and number of boxes, 
        otherwise we simply continue to the next year. 
        At the end of the year range, we print the number of candles left and the total number of boxes bought.


+ count_digits.py:
    
    <-> This program reads a positive integer as input from a user, then prints the number of zeros, odd digits, and even digits of
        the integer.
    
    <-> First we read input from the user as a string. Secondly we check if it is a digit or not. if false, we move to a while loop 
        inside of a try-except block to prompt for input until satisfactory conditions are meto We also take the absolute value of the 
        input integer in the case of a negative input. We the convert the integer back into a string to iterate over each digit. 
        A dictionary with the keys "Zeros","Even",and "Odd" and the value 0 set initially to each is used to iterate over the digits
        classify each. Once the digit corresponds to one of the category keys, we increment it by 2.
        Once all digits have been classified, 
        After this,we print the keys and values using the items() method. 


+ drunken_sailor.py:
    
    <-> This program simulates the random walks of druken sailors on a grid plane. 
        A 'random walk' is basically a sequence of steps in some enclosed plane, where
        the direction of each step is random. The walk terminates when a maximal number
        of steps have been taken or when a step goes outside the given boundary of the plane.
        This program assumes a grid plane with center (0,0).The size of the plane (k) is user determined
        and means a plane with boundaries x,y such that |x|<=|k|, |y|<=|k|, k>0.
    
    <-> Firstly we I make a class called 'drunk' to represent each instance of a sailor. This class takes the number of steps possible as an 
        argument, and contains a number of variablesand one method called 'walk' to respresent the random walk loop. The drunk class contains
        variables to track the x and y positions of the instance on the grid plain, a bolean indicating whether it's considered overboard or 
        not and the number of steps left to take for that instance. The class also contains a method 'walk' which takes the size of the grid
        plain as an argument. While there are steps left to take, we take a step in any direction and subtract it from the total. If our 
        instance ends up outside the spwecified plain, we set our overboard variable to true and break.
        I made a simple parser which only allows the user to continue after specifying an integer. We take in the number of sailors, 
        the size of the plain and the number of steps, and iterate over a range of the sailors, calling walk() for each. We count each 
        that ends up overboard and we give a percentage at the end.  

+ pi_approx.py:
    <-> This program approximates value for pi via the ratio of points plotted on a cartesian plane inside of a unit square containing a unit circle.
        The ratio of points plotted within the square which are also within the circle against those plotted altogether within the square, is roughly 
        equal to the ratio of the circle's area to the sqaure's.This should then roughly equal pi given enough points.

    <-> Since we're checking for three different numbers of points plotted, it's better to make a function to reuse. First I use a list comprehension
        and a zip to iterate over our given number and get our x and y points. Any points with a distance of 1 or less from our origin are inside the circle.
        For each point, we check if the value is less than 1, if yess we count it. a tthe end of the iteration, we find the fraction of this count over our 
        given number of points. We call this for 10, 10000 and 1000000 points. 

+