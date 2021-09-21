__author__ = "Tadj Cazaubon"


"""
This program reads a positive integer as input from a user, then prints the number of zeros, odd digits, and even digits of the integer.
"""

#Get input integer from user
intin = input("\n> Please enter a large integer: ")


try:
    #See if all characters are digits in input
    if intin.isdigit():
        #Try to get absolute value, incase given input is negative
        intin = abs(int(intin))
    else:
        raise Exception


except Exception:

    #While the input is not all digitsa, the loop will continue to prompt the user for a new input
    while intin.isdigit() == False:

        intin = input("\n> Please make sure input is an positive integer: ")
        
        try:
            #See if all characters are digits in input
            if intin.isdigit():
                #Try to get absolute value, incase given input is negative
                intin = abs(int(intin))
                #Break the loop
                break
            else:
                raise Exception

        except Exception:
            #Prompt user for new input
            print("\n Input must be a positive integer: ")
        
#Convert the input back to string to iterate over characters
intin = str(intin)
#We store each of our table rows aas a key-value pair
intdict = {'Zeros':0,'Odd':0,'Even':0}

for digit in intin:
    if int(digit) == 0:
        intdict['Zeros']+=1

    elif int(digit)%2 == 0:
        intdict['Even']+=1
    
    else:
        intdict['Odd']+=1

print("\n")
for key,value in intdict.items():
    print(f" {key} : {value}")
print("\n")