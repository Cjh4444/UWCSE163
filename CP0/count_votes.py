def count_votes(votes):
    results = [0] * (max(votes) + 1)
    for i in votes:
        results[i] += 1
    return results

assert count_votes([1, 0, 1, 1, 2, 0]) == [2, 3, 1]