__author__ = "Tadj Cazaubon"

"""
Program reads a positive odd integer from the keyboard,
prints two triangles. First a right-angled triangle,
then an isosceles triangle.
"""

from math import ceil
from sys import exit

"""
Layers is initialized as None so it can be compared without throwing an error
"""
layers = None


"""While loop to make sure input is an odd, positive integer."""
while type(layers) != int or layers % 2 == 0 or layers < 0:

    try:
        layers = input("\nInput an odd positive integer: ")
        """
        See if input can be represented as an int, if not, raise Exception
        """
        layers = int(layers)
        """If input is even, raise General Exception"""
        if layers % 2 == 0:
            raise Exception
        """If input is negative, raise General Exception"""
        if layers < 0:
            raise Exception

    except Exception:
        print("\n>>> ERROR: Input must be odd and positive \n")
        exit(1)


"""Function to create right angle triangles"""


def right_angle(layers):

    """
    We start fron the top layer with the most elemnts, then remove
    as we iterate down the list of layers until ther is only one left.
    """

    print("\n Right-Angled Tringle:\n")

    layer_number = 1
    """Top layer of triangle with the given number of elements created"""
    full_layer = ["*" for number in range(0, layers)]
    full_layer_str = ' '.join(str(x) for x in full_layer)
    """Print the top layer"""
    print(full_layer_str)

    """Our range starts from 1, because our layers are zero indexed"""
    for layer in range(1, layers):
        """In each layer, an element is replaced via the layer number"""
        full_layer[layer_number-1] = " "
        full_layer_str = ' '.join(str(x) for x in full_layer)
        print(full_layer_str)
        """layer number increment for next loop"""
        layer_number += 1


"""Function to create isocilles triangle with a given number of layers"""


def isocilles(layers):
    layer_list = []
    layer_number = 0
    backwards = -1
    print("\n Isosceles Triangle:\n")
    """
    Full layer of elemnts created
    """
    full_layer = ["*" for number in range(0, layers)]
    full_layer_str = ' '.join(str(x) for x in full_layer)

    """
    First unchanged layer is added to list of layers
    """
    layer_list.append(full_layer_str)

    """
    Isocilles triangles have half as many layers as elements in
    its largest layer. Therefore we iterate over a range of half
    our layer number

    We replace the elements on both ends of each layer, forward
    using positive incrementing of their indexes, and backwards
    using negative incrementation of negative indexes"""
    for layer in range(1, ceil(layers/2)):

        """
        Replace the front and back element with empty space,
        then increment the indexes
        """
        full_layer[layer_number] = " "
        full_layer[backwards] = " "
        layer_number += 1
        backwards -= 1
        """Once the layer is changed, it's saved to the list of layers"""
        full_layer_str = ' '.join(str(x) for x in full_layer)
        layer_list.append(full_layer_str)
        # print(full_layer_str)

    backwards = -1
    for layer in layer_list:
        """
        The list of layers is iterated over but is printed out in
        reverse order using nagative indexes.
        """
        print(layer_list[backwards])
        backwards -= 1

    print("\n")


right_angle(layers)
isocilles(layers)
