from web_scrape import get_selector_table
import my_set_client as my_set_client


def print_stats(cms, counts):
    """
    cms = the count_min_sketch of all the word counts
    counts = dictionary of true word counts
    """
    exact = 0
    total_diff = 0
    incorrect = 0
    max_diff = 0
    total = 0

    for word in counts.keys():
        cms_val = cms.get(word)
        val = counts[word]
        total += val
        if cms_val != val:
            incorrect += 1
            diff = cms_val - val
            if diff > max_diff:
                max_diff = diff
            total_diff += diff
        else:
            exact += 1

    print(f"Exact = {exact}")
    print("Exact% {:.2f}".format(100 * exact / len(counts)))
    print(f"incorrect = {incorrect}")
    print("Avg diff = {:.2f}".format(total_diff / incorrect))
    print(f"Max diff = {max_diff}")
    print("Avg count = {:.2f}\n".format(total / len(counts)))


def main():
    print(get_selector_table())
    my_set_client.main()


if __name__ == "__main__":
    main()
