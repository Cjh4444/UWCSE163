"""
Camden Harris
CSE 163 AX
Implementation of function to find the range between the highest and lowest
numbers in a list
"""


def find_range(list: list) -> list:
    """
    Returns the range of values in a list between the largest and smallest
    numbers of a list of the list
    Keyword arguments:
    list -- list of numbers to find the range of
    """
    return max(list) - min(list) + 1


def main():
    assert find_range([12, 17, 6]) == 12
    assert find_range([5, 20, 7]) == 16
    assert find_range([1]) == 1
    assert find_range([7, 7, 7]) == 1


if __name__ == "__main__":
    main()
