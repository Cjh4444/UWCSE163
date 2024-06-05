"""
Camden Harris
CSE 163 AX
This program implements the functions for the manual half of HW2
"""


def species_count(data: list) -> int:
    """
    Returns the number of unique pokemon
    Keyword arguments:
    data -- parsed csv data
    """
    return len({pokemon["name"] for pokemon in data})


def max_level(data: list) -> tuple:
    """
    Returns the name of level of the pokemon with the highest level
    Keyword arguments:
    data -- parsed csv data
    """
    max_level = 0
    max_name = ""
    for pokemon in data:
        level = pokemon["level"]
        if level > max_level:
            max_level = level
            max_name = pokemon["name"]
    return max_name, max_level


def filter_range(data: list, lower: int, upper: int) -> list:
    """
    Returns the names of pokemon within a level range
    Keyword arguments:
    data -- parsed csv data
    lower -- minimum level (inclusive)
    upper -- maximum level (exclusive)
    """
    return [
        pokemon["name"]
        for pokemon in data
        if lower <= pokemon["level"] < upper
    ]


def mean_attack_for_type(data: list, pokemon_type: str) -> float | None:
    """
    Returns the average attack level for a given type
    Keyword arguments:
    data -- parsed csv data
    pokemon_type -- given pokemon type
    """
    attack_list = [
        pokemon["atk"] for pokemon in data if pokemon["type"] == pokemon_type
    ]

    return None if not attack_list else sum(attack_list) / len(attack_list)


def count_types(data: list) -> dict:
    """
    Returns a dictionary of each type with the value as the number of instances
    Keyword arguments:
    data -- parsed csv data
    """
    type_dictionary = dict()
    for pokemon in data:
        type_dictionary[pokemon["type"]] = (
            type_dictionary.get(pokemon["type"], 0) + 1
        )
    return type_dictionary


def mean_attack_per_type(data: list) -> dict:
    """
    Returns a dictionary of each type with the value as the mean attack level
    Keyword arguments:
    data -- parsed csv data
    """
    types_set = {pokemon["type"] for pokemon in data}
    return {type: mean_attack_for_type(data, type) for type in types_set}
