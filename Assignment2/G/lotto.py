__author__ = "Tadj Cazaubon"

from random import randint

numbers = []

for _ in range(7):
    rando = randint(1,35) 
    
    while rando in numbers:
        rando = randint(1,35)

    numbers.append(rando)

str_nums = [str(num) for num in numbers]

str_nums = ' '.join(str_nums)

print(f"\nThe lotto numbers this week:\n{str_nums}\n")