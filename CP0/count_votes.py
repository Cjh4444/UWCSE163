"""
Camden Harris
"""

def count_votes(votes):
    results = [0] * 3
    for i in votes:
        results[i] += 1
    return results


def main():
    assert count_votes([1, 0, 1, 1, 2, 0]) == [2, 3, 1]


if __name__ == "__main__":
    main()
