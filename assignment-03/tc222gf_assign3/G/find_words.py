__author__ = "Tadj Cazaubon"

"""
This program identifies individual words in a text and store
these words in a separate text file.
"""

import os
import csv


def read_file(file_path):
    string_lists = list()
    # If file doesn't exist, we return None
    # If file exists, read line by line and return list of rows.
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                string_lists.append(line.strip())
        return string_lists
    else:
        print("Path to file does not exist.")
        return None


def get_words(row: list):
    final_row = list()
    row = row.split(' ')
    row = [element.strip() for element in row]
    row = [element for element in row if element.isascii() and not element.isdigit()]

    for element in row:
        # Make sure each element either has apostrophe or is alphanumeric
        for ch in ['\\', '`', '|', '*', '_', '{', '}', '[', ']', '(', ')', '>', '#', '+', '-', '.', ',', '!', '$', '\'', ':',' ']:
            if ch in element:
                # If character in element replace it with nothing.
                element = element.replace(ch, '')
        # Make element lowercase
        element = element.lower()
        # Make sure element is not empty, or a digit.
        if element != '' and not element.isdigit():
            final_row.append(element)

    #final_row = [element for element in row if element != '']
    # final_row = ' '.join(final_row)
    return final_row


def save_words(path, words):
    with open(path, 'w',newline = '') as file:
        # Write the files words with a delimiter
        writer = csv.writer(file, delimiter=";")
        writer.writerow(list(words))


def main(read_name, save_name):
    # Localize directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    texts_path = os.getcwd() + "/large_texts/"
    path = texts_path + read_name

    # Read text files
    rows = read_file(path)
    words = list()
    for row in rows:
        w = get_words(row)
        words += w

    # Save words in file
    outpath = texts_path + save_name
    save_words(outpath, words)
    print(f"Saved {len(words)} words in file {outpath}")


if __name__ == "__main__":
    # Call main for whichever directory needed
    main('holy_grail.txt', 'holy_grail_words.csv')
    main('eng_news_100K-sentences.txt', 'eng_news_100K-sentences_words.csv')
