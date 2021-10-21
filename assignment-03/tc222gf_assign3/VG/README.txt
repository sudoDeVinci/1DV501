This file is a short list and description of the solutions to each VG python script
for Assignment 3.

+ pretty_print_subdirectories.py:

    <-> This program recursively prints an indented mapping of the subdirectories of a given directory.
        Directory depth is shown via indentation. It avoids printing hidden directories.
    
    <-> The spaces needed for a specific level are tracked by a global variable. the directory is passed an an arg, and 
        a space is added whenever the function is called. When the function ends, two spaces are taken away. We use os.scandir
        and loop over the entries.
        If the directory name starts with a dot or hyphen, it's a hidden directory and we skip it entirely. If the entry is a file,
        we print the name using .name along with the spaces. If a directory, we recursively call the function.


+ letter_count.py:

    <-> This program reads text files and generates a distribution of the letters used within it.

    <-> First we generate a dictionary with every letter as a key and initialize each value to 0. Then we loop over the text and 
        tally each letter in our dictionary.  After this, we can pass this dictionary to a function to print the key to each value pair,
        along with a scaled number of symbols to represent its tally.


+ count_lines.py:

    <-> This program houses a function count_py_lines(dir_path) returning a count of all the non-empty lines in all Python files 
        (ending with .py) in the directory specified by dir_path and all its subdirectories.

    <-> Within the function count_py_lines, first we scan the given directory. If the entry is a hidden file, we continue looping. If it's a directory, we 
        recursively call our function within itself. If it's a file, we check if it's a '.py' file, in which case we read it line by line.
        We check if each line is empty, in which case we continue looping, whereas we increment a count for 