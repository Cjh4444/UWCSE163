"""
Camden Harris
CSE 163 AX
Tester file for functions in hw2_manual.py and hw2_pandas
"""

import pandas as pd

from cse163_utils import assert_equals, parse

import hw2_manual
import hw2_pandas


# Your tests here!
def species_count_test(
    data: dict, df: pd.DataFrame, self_data: dict, self_df: pd.DataFrame
):
    """
    Runs test cases for species_count function
    """

    # tests on given pokemon_test.csv data
    assert_equals(hw2_manual.species_count(data), 3)
    assert_equals(hw2_pandas.species_count(df), 3)

    # tests on custom pokemon_self_tests.csv data
    assert_equals(hw2_manual.species_count(self_data), 5)
    assert_equals(hw2_pandas.species_count(self_df), 5)

    print("species count passed all tests")


def max_level_test(
    data: dict, df: pd.DataFrame, self_data: dict, self_df: pd.DataFrame
):
    """
    Runs test cases for max_level function
    """
    # tests on given pokemon_test.csv data
    assert_equals(hw2_manual.max_level(data), ("Lapras", 72))
    assert_equals(hw2_pandas.max_level(df), ("Lapras", 72))

    # tests on custom pokemon_self_tests.csv data
    assert_equals(hw2_manual.max_level(self_data), ("Unfezant", 82))
    assert_equals(hw2_pandas.max_level(self_df), ("Unfezant", 82))

    print("max level passed all tests")


def filter_range_test(
    data: dict, df: pd.DataFrame, self_data: dict, self_df: pd.DataFrame
):
    """
    Runs test cases for filter_range function
    """

    # tests on given pokemon_test.csv data
    assert_equals(
        hw2_manual.filter_range(data, 35, 72),
        ["Arcanine", "Arcanine", "Starmie"],
    )
    assert_equals(
        hw2_pandas.filter_range(df, 35, 72),
        ["Arcanine", "Arcanine", "Starmie"],
    )

    # tests on custom pokemon_self_tests.csv data
    assert_equals(
        hw2_manual.filter_range(self_data, 12, 82),
        ["Exeggutor", "Ninetales", "Charmander", "Charmander"],
    )
    assert_equals(
        hw2_pandas.filter_range(self_df, 12, 82),
        ["Exeggutor", "Ninetales", "Charmander", "Charmander"],
    )

    print("filter range passed all tests")


def mean_attack_for_type_test(
    data: dict, df: pd.DataFrame, self_data: dict, self_df: pd.DataFrame
):
    """
    Runs test cases for mean_attack_for_type function
    """

    # tests on given pokemon_test.csv data
    assert_equals(
        hw2_manual.mean_attack_for_type(data, "fire"),
        47.5,
    )
    assert_equals(
        hw2_pandas.mean_attack_for_type(df, "fire"),
        47.5,
    )

    # tests on custom pokemon_self_tests.csv data
    assert_equals(
        hw2_manual.mean_attack_for_type(self_data, "fire"),
        93 + 1 / 3,
    )
    assert_equals(
        hw2_pandas.mean_attack_for_type(self_df, "fire"),
        93 + 1 / 3,
    )

    print("mean attack for type passed all tests")


def count_types_test(
    data: dict, df: pd.DataFrame, self_data: dict, self_df: pd.DataFrame
):
    """
    Runs test cases for count_types function
    """

    # tests on given pokemon_test.csv data
    assert_equals(
        hw2_manual.count_types(data),
        {"fire": 2, "water": 2},
    )
    assert_equals(
        hw2_pandas.count_types(df),
        {"fire": 2, "water": 2},
    )

    # tests on custom pokemon_self_tests.csv data
    assert_equals(
        hw2_manual.count_types(self_data),
        {"water": 1, "grass": 1, "flying": 1, "fire": 3},
    )
    assert_equals(
        hw2_pandas.count_types(self_df),
        {"water": 1, "grass": 1, "flying": 1, "fire": 3},
    )

    print("count types passed all tests")


def mean_attack_per_type_test(
    data: dict, df: pd.DataFrame, self_data: dict, self_df: pd.DataFrame
):
    """
    Runs test cases for mean_attack_per_type function
    """

    # tests on given pokemon_test.csv data
    assert_equals(
        hw2_manual.mean_attack_per_type(data),
        {"fire": 47.5, "water": 140.5},
    )
    assert_equals(
        hw2_pandas.mean_attack_per_type(df),
        {"fire": 47.5, "water": 140.5},
    )

    # tests on custom pokemon_self_tests.csv data
    assert_equals(
        hw2_manual.mean_attack_per_type(self_data),
        {"water": 51, "grass": 120, "flying": 112, "fire": 93 + 1 / 3},
    )
    assert_equals(
        hw2_pandas.mean_attack_per_type(self_df),
        {"water": 51, "grass": 120, "flying": 112, "fire": 93 + 1 / 3},
    )

    print("mean attack per type passed all tests")


def main():
    """
    main function to run all test cases
    """
    # Call your test functions here!
    data = parse("HW2/pokemon_test.csv")
    df = pd.read_csv("HW2/pokemon_test.csv")
    self_data = parse("HW2/pokemon_self_tests.csv")
    self_df = pd.read_csv("HW2/pokemon_self_tests.csv")

    species_count_test(data, df, self_data, self_df)
    max_level_test(data, df, self_data, self_df)
    filter_range_test(data, df, self_data, self_df)
    mean_attack_for_type_test(data, df, self_data, self_df)
    count_types_test(data, df, self_data, self_df)
    mean_attack_per_type_test(data, df, self_data, self_df)


if __name__ == "__main__":
    main()
