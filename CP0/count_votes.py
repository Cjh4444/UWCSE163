"""
Camden Harris
CSE 163 AX
Implementation of function to sum the results of an election
"""


def count_votes(votes: list) -> list:
    """
    Counts the number of instances of each number between 0-2 (inclusive) in a
    list and returns a list with the count at that number's index
    Keyword arguments:
    votes -- list of votes
    """
    results = [0] * 3
    for i in votes:
        results[i] += 1
    return results


def main():
    assert count_votes([1, 0, 1, 1, 2, 0]) == [2, 3, 1]


if __name__ == "__main__":
    main()
