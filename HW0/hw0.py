"""
Camden Harris
CSE 163 AX
This program implements the functions for HW0
"""


def funky_sum(a: float, b: float, mix: float):
    """
    Returns a linear interpolation between 2 numbers
    Keyword arguments:
    a -- first number
    b -- second number
    mix -- mixing factor for a and b, 0 uses all of b, 1 uses all of a,
            anything in between uses a mix of both
    """
    mix = max(0, min(1, mix))
    return (1 - mix) * a + mix * b


def total(n: int):
    """
    Returns the sum of integers between 0 and n (inclusive)
    Keyword arguments:
    n - largest number
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


def swip_swap(source: str, c1: str, c2: str) -> str:
    """
    Returns the source string with the specified characters swapper
    Keyword arguments:
    c1 - first character
    c2 - second character
    """
    source = source.replace(c1, "\0")
    source = source.replace(c2, c1)
    source = source.replace("\0", c2)
    return source
