"""
Student Name
"""

# this file is excluded from flake8
# The tests you create will be graded

from cse163_utils import assert_equals

from document import Document

# from search_engine import SearchEngine


# This file is left blank for you to fill in with your tests!

doc1 = Document("HW4/test_corpus/document1.txt")
doc2 = Document("HW4/test_corpus/document2.txt")
doc3 = Document("HW4/test_corpus/document3.txt")

assert_equals(1 / 3, doc1.term_frequency("bruno"))
assert_equals(1 / 4, doc2.term_frequency("dog"))
assert_equals(2 / 5, doc3.term_frequency("like"))
