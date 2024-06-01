"""
Student Name
"""

# this file is excluded from flake8
# The tests you create will be graded

from cse163_utils import assert_equals

from document import Document
from search_engine import SearchEngine

# from search_engine import SearchEngine


# This file is left blank for you to fill in with your tests!


def main():
    """
    Runs self-made test cases
    """

    # loading in documents
    doc1 = Document("test_corpus/document1.txt")
    doc2 = Document("test_corpus/document2.txt")
    doc3 = Document("test_corpus/document3.txt")

    # term frequency testing
    assert_equals(1 / 3, doc1.term_frequency("bruno"))
    assert_equals(1 / 4, doc2.term_frequency("dog"))
    assert_equals(2 / 5, doc3.term_frequency("like"))

    # path testing
    assert_equals("test_corpus/document1.txt", doc1.get_path())
    assert_equals("test_corpus/document2.txt", doc2.get_path())
    assert_equals("test_corpus/document3.txt", doc3.get_path())

    # search engine testing
    engine = SearchEngine("Harris_Testing/")
    assert_equals(
        ["Harris_Testing/hello.txt", "Harris_Testing/introduction.txt"],
        engine.search("hello"),
    )
    assert_equals(
        ["Harris_Testing/goodbye.txt", "Harris_Testing/hello.txt"],
        engine.search("goodbye"),
    )
    assert_equals(
        ["Harris_Testing/introduction.txt"],
        engine.search("my"),
    )


if __name__ == "__main__":
    main()
