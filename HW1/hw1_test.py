"""
Camden Harris
CSE 163 AX
This program contains the tests for the hw1.py file
"""

import hw1

from cse163_utils import assert_equals


def test_total():
    """
    Tests the total method
    """
    # The regular case
    assert_equals(15, hw1.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, hw1.total(1))
    assert_equals(0, hw1.total(0))

    # Test the None case
    assert_equals(None, hw1.total(-1))


def test_count_divisible_digits():
    """
    Runs test cases for count_divisible_digits function
    """
    assert_equals(4, hw1.count_divisible_digits(650899, 3))
    assert_equals(1, hw1.count_divisible_digits(-204, 5))
    assert_equals(0, hw1.count_divisible_digits(24, 5))
    assert_equals(0, hw1.count_divisible_digits(1, 0))
    assert_equals(0, hw1.count_divisible_digits(371293, 4))
    assert_equals(1, hw1.count_divisible_digits(0, 4))
    assert_equals(2, hw1.count_divisible_digits(12345, 2))
    assert_equals(1, hw1.count_divisible_digits(12345, 4))
    assert_equals(0, hw1.count_divisible_digits(12345, 6))
    assert_equals(5, hw1.count_divisible_digits(11111, 1))
    assert_equals(0, hw1.count_divisible_digits(12345, 0))
    assert_equals(0, hw1.count_divisible_digits(2, 3))
    assert_equals(1, hw1.count_divisible_digits(3, 3))
    assert_equals(1, hw1.count_divisible_digits(0, 3))
    assert_equals(10, hw1.count_divisible_digits(5555555555, 5))
    assert_equals(0, hw1.count_divisible_digits(1111111111, 2))
    assert_equals(1, hw1.count_divisible_digits(0, 1))
    assert_equals(0, hw1.count_divisible_digits(1234567890, 0))
    print("count passed all tests")


def test_is_relatively_prime():
    """
    Runs test cases for is_relatively_prime function
    """
    assert_equals(True, hw1.is_relatively_prime(12, 13))
    assert_equals(False, hw1.is_relatively_prime(12, 14))
    assert_equals(True, hw1.is_relatively_prime(5, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 1))
    assert_equals(True, hw1.is_relatively_prime(1, 8))
    assert_equals(False, hw1.is_relatively_prime(14, 12))
    print("prime passed all tests")


def test_travel():
    """
    Runs test cases for travel function
    """
    assert_equals((-1, 4), hw1.travel("NW!ewnW", 1, 2))
    assert_equals((0, 0), hw1.travel("", 0, 0))
    assert_equals((5, 8), hw1.travel("NSEW", 5, 8))
    print("travel passed all tests")


def test_reformat_date():
    """
    Runs test cases for reformat_date function
    """
    assert_equals(
        "31/12/1998", hw1.reformat_date("12/31/1998", "M/D/Y", "D/M/Y")
    )
    assert_equals("3/1/2", hw1.reformat_date("1/2/3", "M/D/Y", "Y/M/D"))
    assert_equals("4/0", hw1.reformat_date("0/200/4", "Y/D/M", "M/Y"))
    assert_equals("2", hw1.reformat_date("3/2", "M/D", "D"))
    assert_equals("10", hw1.reformat_date("10", "D", "D"))
    assert_equals("07/09/05", hw1.reformat_date("09/07/05", "M/D/Y", "D/M/Y"))
    print("reformat date passed all tests")


def test_longest_word():
    """
    Runs test cases for longest_word function
    """
    assert_equals("3: Merrily,", hw1.longest_word("song.txt"))
    assert_equals("3: everywhere", hw1.longest_word("little_lamb.txt"))
    assert_equals("1: crawled", hw1.longest_word("spider.txt"))
    assert_equals(None, hw1.longest_word("blank.txt"))
    print("longest word passed all tests")


def test_get_average_in_range():
    """
    Runs test cases for get_average_in_range function
    """
    assert_equals(5.5, hw1.get_average_in_range([1, 5, 6, 7, 9], 5, 7))
    assert_equals(2.0, hw1.get_average_in_range([1, 2, 3], -1, 10))
    assert_equals(0, hw1.get_average_in_range([435, 312, 1620, 1150], 0, 100))
    assert_equals(0, hw1.get_average_in_range([], 3, 5))
    print("average range passed all tests")


def test_mode_digit():
    """
    Runs test cases for mode_digit function
    """
    assert_equals(1, hw1.mode_digit(12121))
    assert_equals(0, hw1.mode_digit(0))
    assert_equals(2, hw1.mode_digit(-122))
    assert_equals(2, hw1.mode_digit(1211232231))
    print("mode digit passed all tests")


def main():
    """
    Main function that runs all test cases
    """
    test_total()
    # Call your test functions here!
    test_count_divisible_digits()
    test_is_relatively_prime()
    test_travel()
    test_reformat_date()
    test_longest_word()
    test_get_average_in_range()
    test_mode_digit()


if __name__ == "__main__":
    main()
