"""
Camden Harris
CSE 163 AX
Implementation of function that finds the location with the largest magnitude
earthquake from a csv file
"""

import cse163_utils


def largest_magnitude(data: list) -> str:
    """
    Returns the name of the location with the greatest magnitude earthquake
    based on the data from a pre-parsed CSV
    Keyword arguments:
    data -- dictionary of CSV data
    """
    largest_magnitude_location = None
    largest_magnitude = 0
    for dict in data:
        if dict["magnitude"] > largest_magnitude:
            largest_magnitude_location = dict["name"]
            largest_magnitude = dict["magnitude"]
    return largest_magnitude_location


def main():
    data = cse163_utils.parse("CP1/Unit 6/largest-earthquake/earthquakes.csv")
    print(largest_magnitude(data))


if __name__ == "__main__":
    main()
