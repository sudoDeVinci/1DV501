__author__ = "Tadj Cazaubon"

"""
This programs reads files and generates a distribution of the letters used.
"""


def word_count(path):
    # dictionary comprehension to initialize keys of a-z
    print(f"\nReading text from file: {path}")
    words = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}

    # Read the file and split its values by a given delimiter
    with open(path, 'r') as file:
        for line in file:
            line = ''.join(line.split())
            for item in line:
                item = item.lower()
                if item in words:
                    words[item] += 1
    total = sum([count for _, count in words.items()])
    print(f"Total number of letters: {total}")
    return words


def generate_graph(words, scale):
    # due to frequencies being in thousands, we scale them down to display
    scaled = {c: int(n/scale) for c, n in words.items()}
    print(f"\nHistogram (each star represents {scale} occurrences of letters)")
    for letter, freq in scaled.items():
        print(f"{letter}  |  {'*'*freq}")


words = word_count("large_texts/holy_grail.txt")
generate_graph(words, 50)
# print(word_count("large_texts/holy_grail.txt"))

words = word_count("large_texts/eng_news_100K-sentences.txt")
generate_graph(words, 10000)
