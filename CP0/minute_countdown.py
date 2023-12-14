"""
Camden Harris
CSE 163 AX
Program to countdown from 60 to 0 (inclusive) in increments of 10
"""


def main():
    print("1 minute countdown")
    for i in range(60, -1, -10):
        print(str(i))
    print("Done!")


if __name__ == "__main__":
    main()
