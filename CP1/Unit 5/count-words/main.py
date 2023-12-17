"""
Camden Harris
CSE 163 AX
Implementation of function that counts the number of unique words in a file
"""
import os


def count_words(file_name: str) -> dict:
    """
    Returns a dictionary of words with the values being the count of that word
    in the given file
    Keyword arguments:
    file_name -- name of file to be read
    """
    word_dict = {}
    file_path = os.getcwd() + "/CP1/Unit 5/count-words/" + file_name
    with open(file_path, "r") as f:
        for word in f.read().split():
            word_dict[word] = word_dict.get(word, 0) + 1
        return word_dict


def main():
    print(count_words("popular_techno_song.txt"))


if __name__ == "__main__":
    main()
