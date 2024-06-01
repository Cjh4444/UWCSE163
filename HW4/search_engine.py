"""
Camden Harris
CSE 163 AX
Data Structure class for Search Engine
"""

# Add your code here
import os
import math
from document import Document
from cse163_utils import normalize_token


class SearchEngine:
    def __init__(self, directory: str) -> None:
        """
        Constructor for a search engine, doing preprocessing to
        create a list of documents as well as an inverted index to
        easily find all documents with a word
        Keyword arguments:
        self - self reference
        director - directory of all documents
        """
        self._inverted_index: dict[str, list] = dict()

        self._documents = [
            Document(os.path.join(directory, filename))
            for filename in os.listdir(directory)
        ]

        for doc in self._documents:
            for word in doc.get_words():
                if word in self._inverted_index:
                    self._inverted_index[word].append(doc)
                else:
                    self._inverted_index[word] = [doc]

    def _calculate_idf(self, word: str) -> float:
        """
        Calculates and returns the inverse document frequency of a given word,
        returns 0 if word is not in any doc
        Keyword arguments:
        self - self reference
        word - word to analyze
        """
        num_docs_with_word = len(
            self._inverted_index.get(normalize_token(word), [])
        )
        if not num_docs_with_word:
            return 0

        return math.log(len(self._documents) / num_docs_with_word)

    def _calculate_tfidf(self, word: str, document: Document) -> float:
        """
        Calculates and returns the term frequency–inverse document frequency of
        a word for a given document, returns 0 if word is not in document
        Keyword arguments:
        self - self reference
        word - word to analyze
        document - document to analyze
        """
        idf = self._calculate_idf(word)

        if not idf:
            return 0

        return idf * document.term_frequency(word)

    def search(self, query: str) -> list[str]:
        """
        Searches for a given query and returns a list
        of document paths in order of relevance
        Keyword arguments:
        self - self reference
        query - query to search documents for
        """
        all_documents_with_a_word: set[Document] = set()
        split_query = query.split(" ")

        for word in split_query:
            all_documents_with_a_word = all_documents_with_a_word.union(
                set(self._inverted_index.get(normalize_token(word), []))
            )

        list_with_scores: list[(Document, float)] = []

        for document in all_documents_with_a_word:
            total_tdidf = 0
            for word in split_query:
                total_tdidf += self._calculate_tfidf(
                    normalize_token(word), document
                )
            list_with_scores.append((document.get_path(), total_tdidf))

        return [
            pair[0]
            for pair in sorted(
                list_with_scores, key=lambda x: x[1], reverse=True
            )
        ]
