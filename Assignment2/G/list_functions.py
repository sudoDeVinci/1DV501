__author__ = "Tadj Cazaubon"

"""
This function houses the definitions of the string function
showed off in 'list_main'.
"""

from random import randint


# Returns a list containing n random integers in the interval 1 to 100.
def random_list(n):
    intlist = [randint(1, 100) for num in range(n)]
    return intlist


# Retuns the average (a rounded off integer) of all values in the list lst.
def average(lst):
    # If an empty list is passed, we return None and give an error
    if len(lst) == 0:
        print("\n>>List empty\n")
        return None
    # Average calculated by dividing list sum over list length
    average = int(sum(lst)/len(lst))
    return average


# This function returns a new list containing only the odd integers in lst
def only_odds(lst):
    odds = [int(x) for x in lst if x % 2 != 0 and x != 0]
    return odds


# Returns a comma separated string representation f the elements in lst
def to_string(lst):
    stringrep = str(lst)
    return stringrep


# This function returns True if a is directly followed by b anywhere in lst
def contains(lst, a, b):
    aindex = 0
    abindicate = False

    # Iteration ends if we reach the last element in the list
    while aindex < (len(lst)-1):
        if lst[aindex] == a:
            if lst[aindex + 1] == b:
                # Once b instance has been found directly after a, we break.
                abindicate = True
                break
        aindex += 1

    return abindicate


# Returns True if lst contains any duplicate elements, otherwise False.
def has_duplicates(lst):

    # Set the boolean to indicate duplicates to false by default
    dupl = False
    Index = 1

    # For each index n, we check if it is in index n+1 onwards.
    for item in lst:
        if item in lst[Index:]:

            dupl = True
            break
        Index += 1
    return dupl
