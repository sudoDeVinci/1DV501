__author__ = "Tadj Cazaubon"

import os

"""
This program contains a recursive function print_subdirectories(dir_path)
that prints the name of all subdirectories for a given directory
and moves on (by calling itself) to print all their subdirectories
(transitively).
"""


spaces = ""


def print_all_subdirectories(path):
    global spaces
    # Whenever thefunction is called, two spaces are added to the indentation.
    spaces += "  "

    entries = os.scandir(path)

    try:
        for entry in entries:
            # Disregard hidden folders
            if entry.name.startswith("_") or entry.name.startswith("."):
                continue
            # If the path is a directory, we call the function within itself.
            if entry.is_dir():
                print(f"{spaces}{entry.name}")
                print_all_subdirectories(entry.path)

            elif entry.is_file():
                print(f"{spaces}{entry.name}")
    except Exception as e:
        print(e)
    # Once all files in directory printed, remove two spaces from indentation.
    spaces = spaces[:-2]


path = os.getcwd()
print_all_subdirectories(path)
