from cse163_utils import assert_equals
from math import sqrt
from time_graph import TimeGraph


# Implement get_primes
def get_primes(max) -> set:
    primes: set = set()
    for i in range(2, max):
        for j in range(2, max):
            if i % j == 0:
                break
        primes.add(i)


def get_primes_sieve(max):
    """
    Return a set of all the prime numbers lower than max. (max is exclusive)

    Create by using the following process/algorithm:
      Fill a set with all numbers starting at 2 and go up to max.
      For every number n still in the set of primes
        remove all multiples of n, but not n itself

    The steps go like this: (This is the Sieve of Eratosthenes)
    Step 1 { 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 }  # fill with all numbers
    Step 2 { 2, 3,    5,    7,    9,     11,     13,     15 }  # remove multiples of 2
    Step 3 { 2, 3,    5,    7,           11,     13         }  # remove multiples of 3
    Etc.
    """
    # Your implementation goes here
    set_of_primes: set = set(range(2, max))

    for i in range(2, max):
        if i in set_of_primes:
            for j in range(i**2, max, i):
                set_of_primes.discard(j)

    return set_of_primes


# Test get_primes as necessary
def test_set_of_primes():
    fiddy = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}
    assert_equals(fiddy, get_primes_sieve(50))
    print("set_of_primes Success")


def hailstone_seq(n):
    """
    n = the max n value to include in the result.
    return a dictionary with the key = number, value = length of sequence.
    next = n / 2     if n is even
    next = n * 3 + 1 if n is odd
    End the sequence when n == 1
    """
    # Your implementation goes here
    hailstone_dict: dict = dict()
    num = 0
    for i in range(1, n + 1):
        num = i
        count = 1
        while num != 1:
            num = (n / 2) if (n % 2 == 0) else (n * 3 + 1)
            count += 1
        hailstone_dict[i] = count

    return hailstone_dict


def graph_prime_performance():
    timer = TimeGraph()
    # timer.time_and_graph(get_primes, "get_primes", max_iters=11)
    timer.time_and_graph(get_primes_sieve, "get_primes_sieve")


def main():
    # once your implementation of getting primes is complete,
    # graph its performance
    # test_set_of_primes()
    graph_prime_performance()


if __name__ == "__main__":
    main()
