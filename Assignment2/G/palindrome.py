__author__ = "Tadj Cazaubon"

"""
This program houses the function is_palindrome(s) that returns True only if the string s is a palindrome.
Along with a short example of how it works.
"""

def is_palindrome(s):
    #We convert all characters to lowercase, remove all spaces, and join each character as long as it is alphabetic
    s = s.lower()
    s = s.replace(' ','')
    s = ''.join([char for char in s if char.isalpha()])

    #Our boolean to determine whether s is a palindrome is set to False by default
    is_pal = False

    #The reverse string is first made as an empty string to append to
    rev_str = ""
    #We will iterate from the last elemnt in s, or the element with an index of -1
    str_index = -1

    for item in s:
        #append each element of s to the reverse string in reverse order 
        rev_str += s[str_index]
        str_index -= 1

    #If our reverse string is equal to s, s is a palindrome
    if rev_str == s:
        is_pal = True
    return is_pal

#print(is_palindrome("Ni talar bra latin!" ))


def main():
    #Example of palindrome in action:
    print("\nThe is_palindrome() function takes a single string as an argument and returns true if it is a palindrome. \n")
    print(f"An example: \n >> Output of is_palindrome('Ni talar bra latin!'): {is_palindrome('Ni talar bra latin!')}")
    print("The function tests the string with the all spaces non alpha-numeric characters removed along with lowered capitalization.\n")

if __name__  == '__main__':
    main()