# Write your function here!
def count_words(file_name):
    word_dict = dict()
    with open("CP1/Unit 5/practice-count-words/" + file_name, "r") as f:
        for line in f:
            for word in line.split():
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
    return word_dict


def main():
    print(count_words("popular_techno_song.txt"))


if __name__ == "__main__":
    main()
