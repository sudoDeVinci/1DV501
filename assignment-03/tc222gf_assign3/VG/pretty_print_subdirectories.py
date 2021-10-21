__author__ = "Tadj Cazaubon"

import os


"""
This program works like print_subdirectories(dir_path) in G but gives
an indented print where the directory depth is given by the indentation
and avoids printing hidden directories.
"""


spaces = ""


def print_all_subdirectories(path):
    # The number of spaces used for the current level
    # Everytime the function is called recursively, a space is added
    global spaces
    spaces += "  "

    entries = os.scandir(path)

    # print(type(entries))
    try:
        for entry in entries:
            # Continue loop if hidden file
            if entry.name.startswith("_") or entry.name.startswith("."):
                continue
            # If directory, print name and
            # recursively call function
            if entry.is_dir():
                print(f"{spaces}{entry.name}")
                print_all_subdirectories(entry.path)
            # If entry is file, print the name
            elif entry.is_file():
                print(f"{spaces}{entry.name}")
    except Exception as e:
        print(e)
    # When all subdirectories iterated through, reduce spaces by two
    spaces = spaces[:-2]


path = os.getcwd()
print_all_subdirectories(path)
