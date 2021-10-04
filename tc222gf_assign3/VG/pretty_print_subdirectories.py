__author__ = "Tadj Cazaubon"

import os

"""
...
"""


spaces = ""


def print_all_subdirectories(path):
    global spaces
    spaces += "  "

    entries = os.scandir(path)
    #listdir = [entry.path for entry in entries]
    #print(listdir)

    #print(type(entries))
    try:
        for entry in entries:
            if entry.name.startswith("_") or entry.name.startswith("."):
                continue
            if entry.is_dir():
                print(f"{spaces}{entry.name}")
                print_all_subdirectories(entry.path)

            elif entry.is_file():
                print(f"{spaces}{entry.name}")
                
    except Exception as e:
        print(e)
        
    spaces = spaces[:-2]

path = os.getcwd()
print_all_subdirectories(path)
