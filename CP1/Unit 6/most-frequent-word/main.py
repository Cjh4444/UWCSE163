"""
Camden Harris
CSE 163 AX
Implementation of function that finds the word with
the most instances from a dictionary
"""


def most_frequent(counts: dict) -> str:
    """
    Returns the string with the most instances based on a dictionary of
    words and their # of occurances
    Keyword arguments:
    counts -- dictionary of words with # of instances
    """
    max_word = None
    max_count = 0
    for word in counts.keys():
        if counts[word] > max_count:
            max_word = word
            max_count = counts[word]
    return max_word


def main():
    word_counts = {"green": 2, "eggs": 6, "and": 3, "yam": 2}
    print(most_frequent(word_counts))


if __name__ == "__main__":
    main()
