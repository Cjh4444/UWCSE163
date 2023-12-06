def find_range(list):
    max = -2**63 - 1
    min = 2**63 - 1

    for i in list:
        max = i if i > max else max
        min = i if i < min else min

    return max - min + 1


def main():
    assert find_range([12, 17, 6]) == 12
    assert find_range([5, 20, 7]) == 16
    assert find_range([1]) == 1
    assert find_range([7, 7, 7]) == 1


if __name__ == "__main__":
    main()
