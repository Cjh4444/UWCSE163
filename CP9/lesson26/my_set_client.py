from lesson26.my_set import MySet


def main():
    s = MySet()
    real_set = set()
    nums = [14, 2, 17, 2]
    query = [14, 2, 17, 12, 4]
    for n in nums:
        s.add(n)
        real_set.add(n)
    print("Length of set:", len(s))
    for n in query:
        print("MySet contains", n, "=>:", n in s)
        print("RealSet contains", n, "=>:", n in real_set)


if __name__ == "__main__":
    main()
