__author__ = "Tadj Cazaubon"

"""
This function houses the definitions of the string function showed off in 'list_main'.
"""

from random import randint


#This function returns a list containing n random integers in the interval 1 to 100.
def random_list(n):
    intlist=[randint(1,100) for num in range(n)]
    return intlist


#This function retuns the average (a rounded off integer) of all values in the list lst.
def average(lst):
    #If an empty list is passed, we return None and give an error
    if len(lst) == 0:
        print("\n>>List empty\n")
        return None
    #The average is calculate by dividing the sum of the list elements byt the length of the list
    average = int(sum(lst)/len(lst))
    return average


#This function returns a new list containing only the odd integers in lst
def only_odds(lst):
    odds = [int(x) for x in lst if x%2!=0 and x!=0]
    return odds


#This function returns a comma separated string representation (a single string) of the elements in lst
def to_string(lst):
    stringrep = str(lst)
    return stringrep


#This function returns True if a is directly followed by b anywhere in the list lst
def contains(lst,a,b):
    aindex=0
    abindicate = False 

    #The iteration ends if we reach the last element in the list, because there's nothing after it to compare 
    while aindex < (len(lst)-1):
        if lst[aindex] == a:
            if lst[aindex+1] == b:
                #Once b instance has been found directly after a, we don't have to keep looping.
                abindicate = True
                break
        aindex+=1

    return abindicate


#This function  returns True if the list lst contains any duplicate elemments, otherwise False.
def has_duplicates(lst):

    #Set the boolean to indicate duplicates to false by default
    dupl = False
    Index = 1

    #For each item in list, with index n, we check if that item is in the sublist of items with index n+1 onwards.
    for item in lst:
        if item in lst[Index:]:
            
            dupl = True
            break
        Index+=1
    return dupl

