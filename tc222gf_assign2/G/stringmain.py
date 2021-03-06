__author__ = "Tadj Cazaubon"

from string_functions import concat, count, reverse
from string_functions import first_last, has_two_X, has_duplicates

"""
This program shows how the different functions defined within
'string_functions' may be used, assuming the arguments passed
to each is correct.
"""

"""
The function concat(s, n) returns the result of concatenating
the string s with itself n times, where n is a positive integer

+ This concatenation will include spaces.
+ Passing 0 as n will lead to no concatenation,
  essentially printing the string s
"""


print("\n      + concat(s,n)")
print(f"\n Using concat() to concatenate 'Ab' 5 times: {concat('Ab', 5)}")
print(f" Using concat() to concatenate 'Ba' 0 times: {concat('Ba', 0)} \n")


"""
The function count(s,x) returns the count the character x occuring in string s.

+ This function is not case sensitive 'A' and 'a' are counted the same.
+ If s is an empty space, return the number of empty spaces in the string.
+ If x is a string rather than a character, the output will be 0
"""


print("\n      + count(x,s)")
print(f"\n count() given 'p' and 'apparent' yields: {count('apparent', 'p')}")
print(f" count() given 'a' and 'Apparent' yields: {count('Apparent', 'a')}")
print(f" count() given 'a' and '  ' yields: {count(' ', 'a')}\n")


"""
The function reverse(s) that returns a string with all
the characters of string s in reverse order.
"""

print("\n      + reverse(s)")
print(f"\n> Using reverse() to reverse 'Example': {reverse('Example')}\n")


"""
The function first_last(s) returns the first and
last characters in the string s in the format (first, last).

+ If only one character is passed, return two identical values.
+ If the passed string is an empty space, returns two empty strings.
"""

print("\n      + first_last(s)")
print(f"\n first_last() given 'Jimmie': {first_last('Jimmie')}")
print(f" first_last() given 'J': {first_last('J')}")
print(f" first_last() given '              ': {first_last(' ')}\n")


"""
The function has_two_X(s) returns True if the string
contains exactly two instances of the character X, otherwise returns False.

+ Function is case sensitive and therefore only counts the capital X characters
+ The function returns false if more than one instance of 'X' is counted.
"""

print("\n      + has_two_X(s)")
print(f"\n has_two_X() to evaluate 'conexxion': {has_two_X('conexxion')}")
print(f" has_two_X() given 'coneXxion': {has_two_X('coneXxion')}")
print(f" has_two_X() given 'coneXXion': {has_two_X('coneXXion')}")
print(f" has_two_X() given 'coneXXXion': {has_two_X('coneXXXion')}\n")


"""
The function has_duplicates(s) returns True if the string s
contains any duplicate characters, otherwise it returns False.

+ Spaces do not count as characters, therefore multiple spaces
  in a string are not counted as duplicates.
"""

print("\n      + has_duplicates(s)")
print(f"\nhas_duplicates() given 'Apology': {has_duplicates('Apology')}")
print(f" has_duplicates() given 'Olof': {has_duplicates('Olof')}")
print(f" has_duplicates() given '    ': {has_duplicates('  ')}\n")
