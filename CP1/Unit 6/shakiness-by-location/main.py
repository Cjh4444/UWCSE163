"""
Camden Harris
CSE 163 AX
Implementation of function to find the total shakiness of location
earthquake from a csv file
"""

import cse163_utils


def shakiness_by_location(data: dict) -> dict:
    """
    Returns a dictionary of locations with the sum of their magnitudes
    based on the data from a pre-parsed CSV
    Keyword arguments:
    data -- dictionary of CSV data
    """
    shakiness_by_location = {}
    for dict in data:
        location = dict["name"]
        magnitude = dict["magnitude"]
        shakiness_by_location[location] = (
            shakiness_by_location.get(location, 0) + magnitude
        )
    return shakiness_by_location


def main():
    data = cse163_utils.parse(
        "CP1/Unit 6/shakiness-by-location/earthquakes.csv"
    )
    print(shakiness_by_location(data))


if __name__ == "__main__":
    main()
