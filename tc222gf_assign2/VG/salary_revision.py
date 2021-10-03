__author__ = "Tadj Cazaubon"

"""
This program takes in whitespace separated integers as input and calulates the mean, median and finally difference between the largest and smallest value.

"""



def parser():

    """
    This function accepts and parses input, asking for correction when the input is not a string of integers separated by whitespaces
    """

    correct = False
    

    while correct == False:
        #Take in our whitespace separated integer values
        salaries = input("\nProvide salaries separated by whitespace, with no commas: ")
        #The values are split into elemtns in a list of the same name
        salaries = salaries.split()

        #each value is checked whether it's a digit or not 
        for salary in salaries:
            if salary.isdigit():
                #if yes for all, the loop will stop and the program continues
                correct = True
            else:
                #If a single value is not a digit, the while loop restarts and the user is prompted for new values
                correct = False
                break
    
    #a new list is made, converting each value to an integer 
    int_salaries = [int(salary) for salary in salaries]
    #We sort our list in ascending order to make calculations down the line easier
    int_salaries = sorted(int_salaries)

    #We return our sortedlist of values
    return int_salaries



def median(sorted_salaries):

    #In a 0 indexed sorted list, the index of the median value can be calculated as below
    
    #Finding the midpoint index of our list
    median_index = (len(sorted_salaries)-1)/2
   
    if len(sorted_salaries)%2 == 0:
        #if our list length is even, we find the average of the integers to the left and right of our index
        rval_index = int(median_index + 0.5)
        lval_index = int(median_index - 0.5)
        middle_avg = (sorted_salaries[lval_index]+sorted_salaries[rval_index])/2
        median_val = int(middle_avg)

    else:
        #if our list is odd, we can simply use the midpoint index to find our median value
        median_val = sorted_salaries[int(median_index)]

    return median_val



def average(sorted_salaries):
    #To find our average, we simply find the sum of the list elements, and divide it by the length of our list
    total = sum(sorted_salaries)
    avg = total/len(sorted_salaries)
    return int(avg)



def gap(sorted_salaries):
    #We find our gap amount by subtracting the last element in our list by the first

    #I opted to find the absolute value as to allow lists in ascending and descedning order to be used here
    gap = int(abs(sorted_salaries[-1]-sorted_salaries[0]))
    return gap



#First we call our parser to get our sorted list of values
int_salaries = parser()

#Now we pass our sorted list to our function calls
print(f"\nMedian: {median(int_salaries)}")
print(f"Average: {average(int_salaries)}")
print(f"Gap: {gap(int_salaries)}\n")