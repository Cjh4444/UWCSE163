"""
Camden Harris
CSE 163 AX
Implementation of function that filters out lines of a specific length
"""
import os


def filter_long_lines(file_name: str, min_words: int) -> None:
    """
    Prints each line in the file with the given name that has
    at least the given number of words in that line.
    Keyword arguments:
    file_name -- name of file to open
    stop -- end of range (exclusive)
    """

    file_path = os.getcwd() + "/CP1/Unit 4/filter-long-lines/" + file_name

    with open(file_path, "r") as f:
        for line in f:
            if len(line.split()) >= min_words:
                print(line, end="")


def main():
    print(os.getcwd())
    filter_long_lines("song.txt", 7)


if __name__ == "__main__":
    main()
