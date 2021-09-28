__author__ = "Tadj Cazaubon"


"""
This program simulates the random walks of druken sailors on a grid plane. 

A 'random walk' is basically a sequence of steps in some enclosed plane, where
the direction of each step is random. The walk terminates when a maximal number
of steps have been taken or when a step goes outside the given boundary of the plane.

This program assumes a grid plane with center (0,0).The size of the plane (k) is user determined
and means a plane with boundaries x,y such that |x|<=|k|, |y|<=|k|, k>0.
"""

from random import randint

"""
Since we needs mutiple instances of essentially the same object performing the same function(s),
it stands to reason to use a class to define the behaviour of a sailor and call the appropritate
methods to make them walk when time.
"""

#Called the class 'drunk' for syntactical reasons later. It defines the behaviour of each drunk sailor.
class drunk:

    #We need to initialize certain class variables
    def __init__(self,steps):
        """
        Our number of steps left will be used during our walk function to check against our moves.
        It is initialized as the maximum number of steps we can make.
        """
        self.steps_left = steps
        #The x and y position are initialized at the center (x,y)
        self.x_position = 0
        self.y_position = 0
        #A boolean to determiner whether thesailor instance is overboard
        self.overboard = False

    def walk(self,plain_size):
        #This method simulates our insatnce walking around our plain with given constraints
        while self.steps_left > 0:
            #For each walk loop, we move between -1 to 1 steps in our x or y directions
            x_steps = randint(-1,1)
            y_steps = randint(-1,1)

            steps_taken = abs(x_steps) + abs(y_steps)

            #If there's only 1 step left, and we are about to move 2 steps, we simply move 1 instead
            if steps_taken > self.steps_left:
                steps_taken = self.steps_left
            
            self.steps_left = self.steps_left - steps_taken
            
            #We update our instance's position
            self.x_position += x_steps
            self.y_position += y_steps

            #If we are not within our plain boundaries, we set our overbaord object variable to True
            if (abs(self.y_position) > abs(plain_size)) or (abs(self.x_position) > abs(plain_size)):
                self.overboard = True
                #Once we're overboard, there's no need to keep iterating
                break



def integer_input(input_message):
    #This ffunction is a simple parser to make sure our input is a positive integer
    while True:
        try:
            
            integer = input(f"{input_message}")

            #Raise a Error if the given int is not a digit
            if integer.isdigit() == False:
                raise Exception
            
            break

        except Exception:
            #exit message for raising error
            print("\n>>>ERROR: Input provided is not an integer\n")

    #Instead of filtering out negative values, we simply return their absolute value
    return abs(int(integer))



def Main():
    #We get our various inputs
    plain_size = integer_input("Enter the size: ")
    steps = integer_input("Enter the number of steps: ")
    walks = integer_input("Enter the number of sailors: ")

    #This stores the number of overboard sailors
    overboard = 0

    #We create the specified number of sailors and make each perform their walk method
    for walk in range(walks):
        
        sailor = drunk(steps)
        sailor.walk(plain_size)
        
        if sailor.overboard == True:
            overboard+=1

    print(f"\nOut of {walks} drunk sailors, {overboard} ({round((overboard/walks)*100,2)}%) fell into the water.\n")



if __name__ == "__main__":
    Main()