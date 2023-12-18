"""
<name>
<period>
<file description>
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
    assert_equals(4, hw1.count_divisible_digits(650899, 3))
    assert_equals(1, hw1.count_divisible_digits(-204, 5))
    assert_equals(0, hw1.count_divisible_digits(24, 5))
    assert_equals(0, hw1.count_divisible_digits(1, 0))
    assert_equals(0, hw1.count_divisible_digits(371293, 4))
    assert_equals(0, hw1.count_divisible_digits(0, 4))
    print("count passed all tests")


def test_is_relatively_prime():
    assert_equals(True, hw1.is_relatively_prime(12, 13))
    assert_equals(False, hw1.is_relatively_prime(12, 14))
    assert_equals(True, hw1.is_relatively_prime(5, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 1))
    assert_equals(True, hw1.is_relatively_prime(1, 8))
    assert_equals(False, hw1.is_relatively_prime(14, 12))
    print("prime passed all tests")


def test_travel():
    assert_equals((-1, 4), hw1.travel("NW!ewnW", 1, 2))
    assert_equals((0, 0), hw1.travel("", 0, 0))
    assert_equals((5, 8), hw1.travel("NSEW", 5, 8))
    print("travel passed all tests")


def test_longest_word():
    assert_equals("3: Merrily,", hw1.longest_word("HW1/song.txt"))
    assert_equals("3: everywhere", hw1.longest_word("HW1/little_lamb.txt"))
    assert_equals("1: crawled", hw1.longest_word("HW1/spider.txt"))
    print("longest word passed all tests")


def test_get_average_in_range():
    assert_equals(5.5, hw1.get_average_in_range([1, 5, 6, 7, 9], 5, 7))
    assert_equals(2.0, hw1.get_average_in_range([1, 2, 3], -1, 10))
    assert_equals(0, hw1.get_average_in_range([435, 312, 1620, 1150], 0, 100))
    assert_equals(0, hw1.get_average_in_range([], 3, 5))
    print("average range passed all tests")


def test_mode_digit():
    assert_equals(1, hw1.mode_digit(12121))
    assert_equals(0, hw1.mode_digit(0))
    assert_equals(2, hw1.mode_digit(-122))
    assert_equals(2, hw1.mode_digit(1211232231))
    print("mode digit passed all tests")


def main():
    test_total()
    # Call your test functions here!
    test_count_divisible_digits()
    test_is_relatively_prime()
    test_travel()
    test_longest_word()
    test_get_average_in_range()
    test_mode_digit()


if __name__ == "__main__":
    main()
