__author__ = "Tadj Cazaubon"

"""Program reads a positive odd integer from the keyboard, and then prints two triangles. First a right-angled triangle, then an isosceles triangle."""

from math import ceil
layers = None

while type(layers)!=int or layers%2==0 or layers<0:
    try:
        layers = input("\n>Input an odd positive integer: ")
        layers = int(layers)
        
        if layers%2==0:
            raise Exception
        
        if layers<0:
            raise Exception

    except Exception:
        print("\n>>> ERROR: Input must be odd and positive")
        



def right_angle(layers):
    print("\n Right-Angled Tringle:\n")
    layer_number = 0
    full_layer = ["*" for number in range(0,layers)]
    full_layer_str = ' '.join(str(x) for x in full_layer)
    print(full_layer_str)


    for layer in range(1,layers):
        layer_number+=1
        full_layer[layer_number-1] = " "
        full_layer_str = ' '.join(str(x) for x in full_layer)
        print(full_layer_str)
    

def isocilles(layers):
    layer_list = []
    layer_number=0
    backwards = -1
    print("\n Isosceles Triangle:\n")
    full_layer = ["*" for number in range(0,layers)]
    full_layer_str = ' '.join(str(x) for x in full_layer)
    layer_list.append(full_layer_str)

    #midpoint = ceil(layers/2)

    #print(full_layer_str)

    for layer in range(1,ceil(layers/2)):
        
        full_layer[layer_number] = " "
        full_layer[backwards] = " "
        layer_number+=1
        backwards-=1
        full_layer_str = ' '.join(str(x) for x in full_layer)
        layer_list.append(full_layer_str)
        #print(full_layer_str)

    backwards = -1
    for layer in layer_list:
        print(layer_list[backwards])
        backwards-=1

    print("\n")


right_angle(layers)
isocilles(layers)