"""
Camden Harris
CSE 163 AX
Implementation of function that returns the list of unique area codes
"""


def area_codes(list: list) -> set:
    """
    Returns a set of unique area codes from a list of phone numbers
    Keyword arguments:
    list -- list of phone number strings
    """
    return set([number.split("-")[0] for number in list])


def main():
    print(
        area_codes(
            ["123-456-7890", "206-123-45676", "123-000-0000", "425-999-9999"]
        )
    )


if __name__ == "__main__":
    main()
