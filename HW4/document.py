"""
Student Name
Intermediate Data Programming
"""

# add your code here
from cse163_utils import normalize_token


class Document:

    def __init__(self, path: str) -> None:
        self._path = path
        with open(self._path) as f:

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
        return self._words_frequency_dict[word]

    def get_path(self) -> str:
        return self._path

    def get_words(self) -> list:
        return list(self._words_frequency_dict.keys())
