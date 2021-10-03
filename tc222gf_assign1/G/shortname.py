__author__ = "Tadj Cazaubon"

"""
Program takes a first name and a last name as two user inputs.
It outputs the first letter of the first name followed by a dot and a space, followed by the first four letters of the last name.
Revised 07/09/21
"""

# names taken from user
first = input("\n> First name: ")
last = input("\n> Last name: ")

# If last name doesn't have four or more letters, then we take the entire name
if len(last) < 4:
    last_rep = last

# slice the last name at the 4th character in the string
else:
    last_rep = last[0:4]

# print result
print(f"\n>Short name: {first[0]}. {last_rep}\n")
