__author__ = "Tadj Cazaubon"

"""
Program will take three integers as user input and determine which one is the largest.
Revised 07/09/21
"""

print("\nPlease provide three integers, A,B and C. \n")

a = int(input("\n> Enter A: "))
b = int(input("\n> Enter B: "))
c = int(input("\n> Enter C: "))

#integers are put into a list to be compared
digit_list= [a,b,c]

#inital digital to be compared is set to the first digit of the list
largest = digit_list[0]

#iterate over the list and replace digit as largest if it is larger than current largest 
for digit in digit_list:
    if digit>largest:
        largest=digit

#print largest
print(f"\n> The largest number is: {largest}\n")