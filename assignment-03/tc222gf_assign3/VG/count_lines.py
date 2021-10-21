__author__ = "Tadj Cazaubon"

"""
This program houses a function count_py_lines(dir_path) returning a count
of all the non-empty lines in all Python files (ending with .py)
in the directory specified by dir_path and all its subdirectories
"""

import os


# counter to track line count
py_lines = 0


def count_py_lines(dir_path):
    global py_lines

    entries = os.scandir(dir_path)

    try:
        for entry in entries:
            # If directory hidden, continue loop
            if entry.name.startswith("_") or entry.name.startswith("."):
                continue
            # If directory, call function recursively
            if entry.is_dir():
                count_py_lines(entry.path)
            elif entry.is_file():
                # If python file, iterate through lines
                if entry.name.endswith(".py"):
                    with open(entry.path, 'r') as file:
                        lines = file.readlines()
                        for line in lines:
                            # If stripped line not blank, increment line count
                            if line != '\n':
                                py_lines += 1
    except Exception as e:
        print(e)
    return py_lines


path = "/home/DeVinci/Desktop/1DV501"
print("Python Line Count: ", count_py_lines(path))
