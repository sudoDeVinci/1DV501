__author__ = "Tadj Cazaubon"

from math import floor

"""
Program reads a number of seconds as an integer and then prints the same amount of time given in hours, minutes and seconds.
Revised 07/09/21
"""

#Time in seconds as user input
secs = int(input("\n > Give a nmber of seconds: "))


#hours are calculated and rounded down
hours = floor(secs/3600)

#Remaining time given hours
secs = secs - (hours*3600)

#minutes calculated and rounded down
minutes = floor(secs/60)

#remaining time in seconds calculated
secs = secs - (minutes*60)




print(f"\n> This corresponds to {hours} hours, {minutes} minutes and {secs} seconds \n")