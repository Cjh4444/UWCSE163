"""
Camden Harris
CSE 163 AX
This program implements the functions for HW0
"""


def species_count(data: list) -> int:
    return len({pokemon["name"] for pokemon in data})


def max_level(data: list) -> tuple:
    max_level = 0
    max_name = ""
    for pokemon in data:
        level = pokemon["level"]
        if level > max_level:
            max_level = level
            max_name = pokemon["name"]
    return max_name, max_level


def filter_range(data: list, lower: int, upper: int) -> list:
    return [
        pokemon["name"]
        for pokemon in data
        if lower <= pokemon["level"] < upper
    ]


def mean_attack_for_type(data: list, type: str) -> float:
    attack_list = [
        pokemon["atk"] for pokemon in data if pokemon["type"] == type
    ]
    return sum(attack_list) / len(attack_list)


def count_types(data: list) -> dict:
    type_dictionary = dict()
    for pokemon in data:
        type_dictionary[pokemon["type"]] = (
            type_dictionary.get(pokemon["type"], 0) + 1
        )
    return type_dictionary


def mean_attack_per_type(data: list) -> dict:
    types_set = {pokemon["type"] for pokemon in data}
    return {type: mean_attack_for_type(data, type) for type in types_set}
