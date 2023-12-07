# Write your function here
def fun_numbers(x, y):
    nums = []
    for i in range(x, y):
        if i % 5 == 0 or i % 2 == 0:
            nums.append(i)
    return nums


def main():
    print(fun_numbers(2, 16))
    print(fun_numbers(5, 5))


if __name__ == "__main__":
    main()
