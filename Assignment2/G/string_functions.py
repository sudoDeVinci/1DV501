__author__ = "Tadj Cazaubon"


"""
This function houses the definitions of
the string function showed off in 'stringmain'.
"""


def concat(s, n):
    # Returns the result of concatenating the string s with itself n times
    s = str(s)
    # Original string is kept as s_original, as s is changed in-place
    s_isolated = s

    # Add the original string to s in-place n times
    s += n*(s_isolated)

    return s


def count(s, x):
    # This function returns the count of character x in the string s.
    s = str(s)
    x = str(x)
    count = 0
    # print(type(x), x)
    for element in s:
        # Make each character lowercase to make the checks not case sensitive.
        if element.lower() == x.lower():
            count += 1

    return count


def reverse(s):
    # This function returns a string with all the characters in s in reverse
    s = list(s)
    # We start iterating from the last element in the string
    rev_s_index = len(s) - 1
    revr = []

    for element in s:
        # Appending strings via indexes in reverse
        revr.append(s[rev_s_index])
        rev_s_index -= 1

    # Join reverse string list and return it
    revr_str = ' '.join(revr)
    return revr_str


def first_last(s):
    # This function returns the first and last characters in the string s.
    s = str(s)

    s_f = s[0]
    s_l = s[-1]

    return s_f, s_l


def has_two_X(s):
    # Return True if s has exactly two instances of 'X', otherwise False

    # Set the boolean for whether there are two X's to false by default
    twoXs = False
    exes = 0
    # create a list
    for x in s:
        if x == 'X':
            exes += 1
        if exes > 2:
            # Once there are more than two x's, we break.
            break
    # Change twoXs to True if exactly two X's are found in the string.
    if exes == 2:
        twoXs = True

    return twoXs


def has_duplicates(s):
    # Return True if the string s contains any duplicates, otherwise False.

    # First we make all characters lowercase, then get rid of any spaces.
    s = str(s).lower()
    s = s.replace(' ', '')

    # Set the boolean to indicate duplicates to false by default
    dupl = False
    Index = 1

    # For each index n in s, we check if that character is in n+1 onwards.
    for x in s:
        if x in s[Index:]:
            # Once a duplicate is found, there's no need to keep iterating
            dupl = True
            break
        Index += 1

    return dupl
