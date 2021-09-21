__author__ = "Tadj Cazaubon"

from random import randint

""" 
This program usesthe random module to simulate trolling two dice 10,000 times. At the same time, keeping track of the number of times you get the result of the sum of the two rolls
(Using a list to store a count of the numbers). After the simulation, the frequencies for the different numbers are presented as a table.
"""
#Variable to store the sum of the two rolls (We start at 2 because that's the smallest sum of two dice)
rollno = 2

#List comprehension of all all 10,000 rolls stored as tuples
dicerolls = [(randint(1,6),randint(1,6)) for (d1,d2) in zip(range(10000),range(10000))]

#Each index n in this list will be used to store a count of the roll frequency of the sum n+1, eg totals[6] will count the number of times 7 has occurred.
totals = [0  for x in range(0,12)]


for roll in dicerolls:
    n1,n2 = roll
    #Getting the sum of diceroll
    rollsum = n1+n2
    #Incrementing index in totals corresponding to the roll frequency
    totals[rollsum-1]+=1


print("\nFrequency table (sum,count) for rolling two dice 10000 times\n")

#We start printing at the index 1 because it stores the values for the sum 2
for count in totals[1:]:
    print(f"{rollno}    {count}")
    rollno+=1

print("\n")
