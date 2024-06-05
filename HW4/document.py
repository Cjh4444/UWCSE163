"""
Camden Harris
CSE 163 AX
Data Structure class for document
"""

# add your code here
from cse163_utils import normalize_token


class Document:

    def __init__(self, path: str) -> None:
        """
        Constructor for a document, doing preprocessing to
        create a frequency dictionary
        Keyword arguments:
        self - self reference
        path - path to desired file
        """
        self._path = path
        with open(self._path, encoding="utf-8") as f:

            _ = dict()
            for line in f:
                for word in line.split():
                    norm_word = normalize_token(word)
                    _[norm_word] = _.get(norm_word, 0) + 1

            num_words = sum(_.values())

            self._words_frequency_dict = {
                word: count / num_words for word, count in _.items()
            }

    def term_frequency(self, word: str) -> float:
        """
        Returns the frequency of a word in a document,
        0 if word is not in the document
        self - self reference
        word - desired word
        """
        return self._words_frequency_dict.get(normalize_token(word), 0)

    def get_path(self) -> str:
        """
        Returns path to file
        self - self reference
        """
        return self._path

    def get_words(self) -> list:
        """
        Returns list of all unique words in document
        self - self reference
        """
        return list(self._words_frequency_dict.keys())
