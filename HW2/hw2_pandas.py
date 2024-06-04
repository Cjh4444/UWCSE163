"""
Camden Harris
CSE 163 AX
This program implements the functions for the pandas half of HW2
"""

from pandas import DataFrame


def species_count(df: DataFrame) -> int:
    """
    Returns the number of unique pokemon
    Keyword arguments:
    df -- dataframe from csv
    """
    return len(df["name"].unique())


def max_level(df: DataFrame) -> tuple:
    """
    Returns the name of level of the pokemon with the highest level
    Keyword arguments:
    df -- dataframe from csv
    """
    max_idx = df["level"].idxmax()
    return df["name"].iloc[max_idx], df["level"].iloc[max_idx]


def filter_range(df: DataFrame, lower: int, upper: int) -> list:
    """
    Returns the names of pokemon within a level range
    Keyword arguments:
    df -- dataframe from csv
    lower -- minimum level (inclusive)
    upper -- maximum level (exclusive)
    """
    is_above_min = lower <= df["level"]
    is_below_max = upper > df["level"]
    return list(df[is_above_min & is_below_max]["name"])


def mean_attack_for_type(df: DataFrame, pokemon_type: str) -> float | None:
    """
    Returns the average attack level for a given type
    Keyword arguments:
    df -- dataframe from csv
    pokemon_type -- given pokemon type
    """
    is_type = df["type"] == pokemon_type
    type_df = df[is_type]

    return None if type_df.empty else df[is_type]["atk"].mean()


def count_types(df: DataFrame) -> dict:
    """
    Returns a dictionary of each type with the value as the number of instances
    Keyword arguments:
    df -- dataframe from csv
    """
    return dict(df["type"].value_counts())


def mean_attack_per_type(df: DataFrame) -> dict:
    """
    Returns a dictionary of each type with the value as the mean attack level
    Keyword arguments:
    df -- dataframe from csv
    """
    return dict(df.groupby("type")["atk"].mean())
