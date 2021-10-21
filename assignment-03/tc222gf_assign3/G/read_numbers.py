__author__ = "Tadj Cazaubon"

"""
This proram reads two files (one after each other) and for each file computes
and presents the average (mean) value and the standard deviation.
"""


def mean(lst):
    # Average of our list values
    avg = sum(lst)/len(lst)
    return round(avg, 3)


def std(lst):
    # We get the average of the listed numbers
    avg = sum(lst)/len(lst)
    total_sqr_dif = 0
    # We get the total square difference of the list elements from the mean
    for element in lst:
        sqr_dif = (element-avg)**2
        total_sqr_dif += sqr_dif
    # From here we get the variance and the standard deviation
    variance = total_sqr_dif/len(lst)
    std_dev = variance**(1/2)
    return round(std_dev, 3)


def read_file(path, delimiter):
    lst = []
    # Read the file and split its values by a given delimiter
    with open(path, 'r') as file:
        for line in file:
            string_line_list = line.split(delimiter)
            for item in string_line_list:
                lst.append(int(item))
    return lst


# Reading the first file separated by commas
lst = read_file("10000_integers/10000integers_A.txt", ",")
avg = mean(lst)
std_dev = std(lst)
print(f"TEXT FILE A \nMean: {avg}   Standard Dev: {std_dev}")

# Reading the second file separated by colons
lst = read_file("10000_integers/10000integers_B.txt", ":")
avg = mean(lst)
std_dev = std(lst)
print(f"TEXT FILE B \nMean: {avg}    Standard Dev: {std_dev}")
