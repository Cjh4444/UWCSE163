# Write your function here!
def count_unique_words(file_name):
    file_set = set()
    with open("CP1/Unit 4/practice-count-unique-words/" + file_name) as f:
        for line in f:
            temp_set = set(line.split())
            file_set.update(temp_set)
    return len(file_set)


def main():
    print(count_unique_words("song.txt"))


if __name__ == "__main__":
    main()
