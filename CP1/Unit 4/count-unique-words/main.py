"""
Camden Harris
CSE 163 AX
Implementation of function that counts the number of unique words in a file
"""

import os


def count_unique_words(file_name: str) -> int:
    """
    Returns the number of unique tokens that appear in that file
    Keyword arguments:
    file_name -- name of file to open
    """
    file_path = os.getcwd() + "/CP1/Unit 4/count-unique-words/" + file_name

    with open(file_path) as f:
        return len(set(f.read().split()))


def main():
    print(count_unique_words("song.txt"))


if __name__ == "__main__":
    main()
