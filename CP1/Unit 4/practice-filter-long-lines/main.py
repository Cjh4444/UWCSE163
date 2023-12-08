def filter_long_lines(file_name, min_words):
    """
    Prints each line in the file with the given name that has
    at least the given number of words in that line.
    """
    # Write your code here :)

    with open("CP1/Unit 4/practice-filter-long-lines/" + file_name, "r") as f:
        print()
        for line in f:
            if len(line.split()) >= min_words:
                print(line, end="")


def main():
    filter_long_lines("song.txt", 7)


if __name__ == "__main__":
    main()
