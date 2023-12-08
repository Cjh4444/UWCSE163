def fibonacci(max_num):
    prev_num, curr_num = 0, 1
    while (curr_num <= max_num):
        prev_num, curr_num = curr_num, curr_num + prev_num
    return curr_num


def main():
    assert fibonacci(3) == 5
    assert fibonacci(6) == 8
    assert fibonacci(-2) == 1


if __name__ == "__main__":
    main()
