__author__ = "Tadj Cazaubon"

"""
This function demonstrates the functionality of the functions defined in list_functions
"""

from list_functions import random_list, average, only_odds, to_string, contains, has_duplicates

"""
The function random_list(n) returns a list containing n random integers in the interval 1 to 100.

+ The input n must be a positive integerS
"""

print("\n    + random_list()")
print(f"\n> Using random_list() to create a list with 5 elements: {random_list(5)}")
print(f"> Using random_list() to create a list with 0 elements: {random_list(0)}\n")


#------------------------------------------------------------------------------------------------------------------------------------------------#


"""
The function average(lst ) returns  the average (a rounded off integer) of all values in the list lst.

+ the lst must contains only integers or floating point numbers.
"""

print("\n     + average(lst)")
print(f"\n> Using average(lst) to find the average of the list [1,2,3,4,5]: {average([1,2,3,4,5])}")
print(f"> Using average(lst) to find the average of the list [17.9,35.6,12.5]: {average([17.9,35.6,12.5])}\n")


#------------------------------------------------------------------------------------------------------------------------------------------------#


"""
The function only_odd(lst) returns a list containing only the odd integers in lst.

+ All elements in lst must either integers or floating point numbers.
"""

print("\n     + only_odd(lst)")
print(f"\n> Using only_odd(lst) to find the odd numbers in the list [0,1,2,3,4]: {only_odds([0,1,2,3,4])}")
print(f"> Using only_odd(lst) to find the odd numbers in list [-17,-35,-12]: {only_odds([-17,-35,-12])}\n")



#------------------------------------------------------------------------------------------------------------------------------------------------#


"""
The function to_string(lst) returns a comma separated string representation (a single string) of the elements in lst. 
For example, to_string([1,2,3]) should return a string "[1,2,3]".
"""

print("\n     + to_string(lst)")
print(f"\n> Using to_string() to convert the list [1,2,3] retuns: {to_string([1,2,3])}\n")
#print(f"\n> Using to_string() to find the average of the list [17.9,35.6,12.5]: {([17.9,35.6,12.5])}\n")


#------------------------------------------------------------------------------------------------------------------------------------------------#


"""
This function contains(lst,a,b) returns True if a is directly followed by b anywhere in the list lst. 
Hence, contains([1,2,3,4],2,3) should return True whereas contains([1,2,3,4],2,4) should return False.
"""

print("\n     + contains(lst,a,b)")
print(f"\n> Using contains() to evaluate [1,2,3,4] with 2,3 as a,b respectively: {contains([1,2,3,4],2,3)}")
print(f"> Using contains() to evaluate [1,2,3,4] with 2,4 as a,b respectively: {contains([1,2,3,4],2,4)} \n")


#------------------------------------------------------------------------------------------------------------------------------------------------#


"""
The function has_duplicates(lst) returns True if the list lst contains any duplicate elemments, otherwise False.

+ Things like empty spaces as elemnts are still counted as elements and therefore can be seen as duplicates if multiple are 
in the list lst.
"""

print("\n     + has_duplicates(lst)")
print(f"\n> Using has_duplicates() to check if there are duplicates in ['A','p','p']: {has_duplicates(['A','p','p'])}")
print(f"> Using has_duplicates() to check if there are duplicates in ['O','l','o']: {has_duplicates(['O','l','o'])}")
print(f"> Using has_duplicates() to check if there are duplicates in [' ',' ',' ']: {has_duplicates([' ',' ',' '])}\n")