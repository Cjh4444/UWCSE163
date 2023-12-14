"""
Camden Harris
CSE 163 AX
Implementation of function to countdown from a number
"""


def countdown(start_time: int) -> None:
    """
    Counts down in increments of 10 from a non-negative number
    Keyword arguments:
    start_time -- starting number to countdown from
    """
    if start_time < 0:
        print("Start must be non-negative!")
        return

    print(str(start_time) + " minute countdown")
    for i in range(start_time, -1, -10):
        print(str(i))
    print("Done!")


def main():
    countdown(60)
    print()
    countdown(15)
    print()
    countdown(-4)
    print()
    countdown(0)


if __name__ == "__main__":
    main()
