"""
Camden Harris
CSE 163 AX
Implementation of function to return a list
of numbers divisible by 5 or 2 in a range
"""


def fun_numbers(start: int, stop: int) -> list:
    """
    returns a list of all “fun” numbers between start (inclusive) and stop
    (exclusive). A number is “fun” if it is divisible by 2 or divisible by 5
    Keyword arguments:
    start -- start of range (inclusive)
    stop -- end of range (exclusive)
    """
    return [i for i in range(start, stop) if (i % 5 == 0 or i % 2 == 0)]


def main():
    print(fun_numbers(2, 16))
    print(fun_numbers(5, 5))


if __name__ == "__main__":
    main()
