__author__ = "Tadj Cazaubon"

"""
This program prints all numbers from 100 to 200
divisble by either 4 or 5, but not both.
"""

"""List all numbers from 100 to 200. We check the boolean state of whether
divisible by 4 and 5. If they are both true or false, we do not add it.
If only one is true, we add it."""
fours_fives = [x for x in range(100, 201) if (x % 4 == 0) != (x % 5 == 0)]

# print(fours_fives)

to_print = []

"""Slice string to represent each line and use join() to change the delimiter
to a space instead of a comma. Each item is added to a string to get rid of
the braces around the lines."""
# print(f"{str(fours_fives[0:10])}\n{str(fours_fives[10:20])}\n{str(fours_fives[20:30])}\n{str(fours_fives[30:])}")
line1 = ' '.join(str(x) for x in fours_fives[0:10])
line2 = ' '.join(str(x) for x in fours_fives[10:20])
line3 = ' '.join(str(x) for x in fours_fives[20:30])
line4 = ' '.join(str(x) for x in fours_fives[30:])

"""print the lines"""
print(f"\n{line1}\n{line2}\n{line3}\n{line4}\n")
