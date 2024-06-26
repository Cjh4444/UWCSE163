"""
Camden Harris
CSE 163 AX
Tester file for functions in hw0.py
"""

import hw0

from cse163_utils import assert_equals


def test_total():
    """
    Runs test cases for test_total function
    """
    # The regular case
    assert_equals(15, hw0.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, hw0.total(1))
    assert_equals(0, hw0.total(0))


def test_funky_sum():
    """
    Runs test cases for funky_sum function
    """
    assert_equals(1, hw0.funky_sum(1, 3, 0))
    assert_equals(3, hw0.funky_sum(1, 3, 1))
    assert_equals(1.5, hw0.funky_sum(1, 3, 0.25))
    assert_equals(3, hw0.funky_sum(1, 3, 2))
    assert_equals(1, hw0.funky_sum(1, 3, -1))


def test_swip_swap():
    """
    Runs test cases for swip_swap function
    """
    assert_equals("offbar", hw0.swip_swap("foobar", "f", "o"))
    assert_equals("foocar", hw0.swip_swap("foobar", "b", "c"))
    assert_equals("ginbgonb", hw0.swip_swap("bingbong", "b", "g"))
    assert_equals("olo", hw0.swip_swap("lol", "l", "o"))


def main():
    """
    main function to run all test cases
    """
    test_total()
    test_funky_sum()
    test_swip_swap()


if __name__ == "__main__":
    main()
