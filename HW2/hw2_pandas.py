"""
Camden Harris
CSE 163 AX
This program implements the functions for HW0
"""

from pandas import DataFrame


def species_count(df: DataFrame) -> int:
    return len(df["name"].unique())


def max_level(df: DataFrame) -> tuple:
    max_idx = df["level"].idxmax()
    return df["name"].iloc[max_idx], df["level"].iloc[max_idx]


def filter_range(df: DataFrame, lower: int, upper: int) -> list:
    is_above_min = lower <= df["level"]
    is_below_max = upper > df["level"]
    return list(df[is_above_min & is_below_max]["name"])


def mean_attack_for_type(df: DataFrame, type: str) -> float:
    is_fire = df["type"] == type
    return df[is_fire]["atk"].mean()


def count_types(df: DataFrame) -> dict:
    return dict(df["type"].value_counts())


def mean_attack_per_type(df: DataFrame) -> dict:
    return dict(df.groupby("type")["atk"].mean())
