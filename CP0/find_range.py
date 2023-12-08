def find_range(list):
    return max(list) - min(list) + 1


def main():
    assert find_range([12, 17, 6]) == 12
    assert find_range([5, 20, 7]) == 16
    assert find_range([1]) == 1
    assert find_range([7, 7, 7]) == 1


if __name__ == "__main__":
    main()
