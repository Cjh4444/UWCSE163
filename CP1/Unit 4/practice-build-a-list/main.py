# Write your function here

def fun_numbers(x, y):
    return [i for i in range(x, y) if (i % 5 == 0 or i % 2 == 0)]


def main():
    print(fun_numbers(2, 16))
    print(fun_numbers(5, 5))


if __name__ == "__main__":
    main()
