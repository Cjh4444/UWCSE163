import pandas as pd
import math
import sys
import cse163_utils

sys.path.append("/Users/camdencambre/UWCSE163/CP2")

import Unit7.lesson7 as lesson7
import Unit8.lesson8 as lesson8


def lesson7_problem_0_test():
    df = pd.read_csv(
        "/Users/camdencambre/UWCSE163/CP2/test/data/earthquakes.csv"
    )
    ans = 1.5129
    ok = math.isclose(ans, lesson7.problem_0(df), abs_tol=0.001)
    cse163_utils.assert_equals(ok, True)
    print("L7 P0 works")


def lesson7_problem_1_test():
    df = pd.read_csv(
        "/Users/camdencambre/UWCSE163/CP2/test/data/earthquakes.csv"
    )
    cse163_utils.assert_equals(3040, lesson7.problem_1(df))
    print("L7 P1 works")


def lesson7_problem_2_test():
    df = pd.read_csv(
        "/Users/camdencambre/UWCSE163/CP2/test/data/earthquakes.csv"
    )
    df_result = lesson7.problem_2(df)
    ids = ["us10006cwy", "us10006cx0", "us10006cxc", "us10006cxf"]
    ser = pd.Series(ids, index=[3877, 3897, 4012, 4036])
    ok = cse163_utils.series_equals(df_result["id"], ser)
    cse163_utils.assert_equals(ok, True)
    print("L7 P2 works")


def lesson7_problem_3_test():
    df = pd.read_csv(
        "/Users/camdencambre/UWCSE163/CP2/test/data/earthquakes.csv"
    )
    index = df["magnitude"].idxmax()
    expected = df.loc[index]
    actual = lesson7.problem_3(df)
    ok = cse163_utils.series_equals(expected, actual)
    cse163_utils.assert_equals(ok, True)
    print("L7 P3 works")


def lesson8_problem_0_test():
    df = pd.read_csv("/Users/camdencambre/UWCSE163/CP2/test/data/ufos.csv")
    ans = df.groupby("shape")["duration (seconds)"].mean()
    result = lesson8.problem_0(df)
    ok = cse163_utils.series_equals(ans, result)
    cse163_utils.assert_equals(ok, True)
    print("L8 P0 works")


def lesson8_problem_1_test():
    df = pd.read_csv("/Users/camdencambre/UWCSE163/CP2/test/data/ufos.csv")
    ans = (
        df[(df["latitude"] > 0) | (df["longitude"] > 0)]
        .groupby("city")["duration (seconds)"]
        .max()
    )
    result = lesson8.problem_1(df)
    ok = cse163_utils.series_equals(ans, result)
    cse163_utils.assert_equals(ok, True)
    print("L8 P1 works")


def lesson8_problem_2_test():
    df = pd.read_csv("/Users/camdencambre/UWCSE163/CP2/test/data/ufos.csv")
    ans = "birmingham (uk/england)"
    result = lesson8.problem_2(df)
    cse163_utils.assert_equals(ans, result)
    print("L8 P2 works")


def lesson8_problem_3_test():
    df = pd.read_csv("/Users/camdencambre/UWCSE163/CP2/test/data/ufos.csv")
    vals = [24, 17, 6, 26, 25, 29, 26, 16, 20, 16]
    ser = pd.Series(vals)
    result = lesson8.problem_3(df)
    ok = cse163_utils.series_equals(ser, result[0:10])
    cse163_utils.assert_equals(ok, True)
    print("L8 P3 works")


def lesson9_problem_1_test():
    # Enter code here
    ok = cse163_utils.compare_plots("prob1.png", "test/prob1.png")
    cse163_utils.assert_equals(ok, True)
    print("L9 P1 works")


def lesson9_problem_2_test():
    ok = cse163_utils.compare_plots("prob2.png", "test/prob2.png")
    cse163_utils.assert_equals(ok, True)
    print("L9 P2 works")


def lesson9_problem_3_test():
    # Enter code here
    ok = cse163_utils.compare_plots("prob3.png", "test/prob3.png")
    cse163_utils.assert_equals(ok, True)
    print("L9 P3 works")


def lesson9_problem_4_test():
    # Enter code here
    ok = cse163_utils.compare_plots("prob4.png", "test/prob4.png")
    cse163_utils.assert_equals(ok, True)
    print("L9 P4 works")


def main():
    lesson7_problem_0_test()
    lesson7_problem_1_test()
    lesson7_problem_2_test()
    lesson7_problem_3_test()
    lesson8_problem_0_test()
    lesson8_problem_1_test()
    lesson8_problem_2_test()
    lesson8_problem_3_test()
    lesson9_problem_1_test()
    lesson9_problem_2_test()
    lesson9_problem_3_test()
    lesson9_problem_4_test()


if __name__ == "__main__":
    main()
