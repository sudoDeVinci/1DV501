__author__ = "Tadj Cazaubon"

from random import randint

class drunk:
    def __init__(self,steps):
        self.steps_left = steps
        self.x_position = 0
        self.y_position = 0
        self.overboard = False

    def walk(self,plain_size):
        
        while self.steps_left > 0:
            x_steps = randint(-1,1)
            y_steps = randint(-1,1)

            steps_taken = abs(x_steps) + abs(y_steps)

            if steps_taken > self.steps_left:
                steps_taken = self.steps_left
            
            self.steps_left = self.steps_left - steps_taken
            
            self.x_position += x_steps
            self.y_position += y_steps

            if (abs(self.y_position) > abs(plain_size)) or (abs(self.x_position) > abs(plain_size)):
                self.overboard = True
                break


def Main():
    plain_size = int(input("\nEnter the size: "))
    steps = int(input("Enter the number of steps: "))
    walks = int(input("Enter the number of sailors: "))


    overboard = 0

    for walk in range(walks):
        
        sailor = drunk(steps)
        sailor.walk(plain_size)
        
        if sailor.overboard == True:
            overboard+=1

    print(f"\nOut of {walks} drunk sailors, {overboard} ({round((overboard/walks)*100,2)}%) fell into the water.\n")



if __name__ == "__main__":
    Main()