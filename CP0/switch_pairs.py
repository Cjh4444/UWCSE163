"""
Camden Harris
CSE 163 AX
Implementation of function to switch every pair of letters
"""


def switch_pairs(word: str) -> str:
    """
    Returns the inputted word with each pair of letters swapped
    Keyword arguments:
    word -- word to base switch off of
    """
    return "".join([word[i+1] + word[i] for i in range(0, len(word) - 1, 2)]) \
        + word[len(word) - 1] if len(word) % 2 == 1 else ""


def main():
    assert switch_pairs("example") == "xemalpe"
    assert switch_pairs("hello there") == "ehll ohtree"


if __name__ == "__main__":
    main()
