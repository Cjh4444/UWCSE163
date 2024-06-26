"""
Camden Harris
CSE 163 AX
This program implements the functions for HW1
"""

# do not import math


def total(n):
    """
    Returns the sum of the numbers from 0 to n (inclusive).
    If n is negative, returns None.
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


def count_divisible_digits(n: int, m: int) -> int:
    """
    Returns the number of digits in n that are divisible by m
    if m is 0, returns 0
    Keyword arguments:
    n -- number made up of digits
    m -- divisor
    """
    if m == 0:
        return 0
    if n == 0:
        return 1

    num_divisible_digits = 0

    n = abs(n)

    while n != 0:
        digit = n % 10
        if digit % m == 0:
            num_divisible_digits += 1
        n //= 10
    return num_divisible_digits


def is_relatively_prime(n: int, m: int) -> bool:
    """
    Returns if n and m are prime relative to each other
    (don't share any common factors)
    Keyword arguments:
    n -- number 1
    m -- number 2
    """
    if (n == 1) or (m == 1):
        return True

    larger_number = max(n, m)
    smaller_number = min(n, m)

    for i in (2, smaller_number):
        if (smaller_number % i) == 0:
            if (larger_number % i) == 0:
                return False
    return True


def travel(directions: str, x: int, y: int):
    """
    Performs directional movement based on a starting point and a string of
    commands using NSEW and returns a tuple of the new position
    Keyword arguments:
    directions -- str of directions to go
    x -- starting x coordinate
    y -- starting y coordinate
    """
    for direction in directions:
        dir_lowercase = direction.lower()
        if dir_lowercase == "n":
            y += 1
        if dir_lowercase == "s":
            y -= 1
        if dir_lowercase == "e":
            x += 1
        if dir_lowercase == "w":
            x -= 1
    return (x, y)


def reformat_date(date: str, old_format: str, new_format: str) -> str:
    """
    Returns a reformatted a date string from an old format to a new one
    Keyword arguments:
    date -- date string
    old_format -- old format of date
    new_format -- new/desired format of date
    """
    format_to_date_dict = {
        old_form: old_date
        for old_form, old_date in zip(
            old_format.split("/"),
            date.split("/"),
        )
    }

    return "/".join(
        [format_to_date_dict[new_form] for new_form in new_format.split("/")],
    )


def longest_word(file_name: str) -> str | None:
    """
    Returns the longest word and it's line location from a file
    Keyword arguments:
    file_name -- name of file to scan
    """

    longest_word = None
    longest_word_length = 0
    line_number_of_word = 0
    with open(file_name, "r") as f:
        for line_num, line in enumerate(f, start=1):
            for word in line.split():
                word_length = len(word)
                if word_length > longest_word_length:
                    longest_word = word
                    longest_word_length = word_length
                    line_number_of_word = line_num
    return f"{line_number_of_word}: {longest_word}" if longest_word else None


def get_average_in_range(values: list, low: int, high: int) -> float:
    """
    Returns the average of the values in a list between bounds
    Keyword arguments:
    list -- list of numbers
    low -- lower bound of range (inclusive)
    high -- upper bound of range (exclusive)
    """
    if len(values) == 0:
        return 0

    sum = 0
    num_terms = 0
    for value in values:
        if low <= value and value < high:
            sum += value
            num_terms += 1
    return sum / num_terms if num_terms > 0 else 0


def mode_digit(n: int) -> int:
    """
    Returns the most common digit in a number, in the instance of a tie
    the larger number is returned
    Keyword arguments:
    n -- number made up of digits
    """
    if n == 0:
        return 0

    n = abs(n)

    digits = [0] * 10
    while n != 0:
        digits[n % 10] += 1
        n //= 10

    max_num = 0
    max_index = 0

    for index, digit in enumerate(digits):
        if digit >= max_num:
            max_num = digit
            max_index = index
    return max_index


# add main-pattern to run outside of Unit Tests, if desired
