import pandas as pd
import math
from cse163_utils import assert_equals


def test_():
    df = pd.read_csv("data/earthquakes.csv")
    ans = 1.5129
    ok = math.isclose(ans, lesson7.problem_0(df), abs_tol=0.001)
    assert_equals(ok, True)


def test_():
    df = pd.read_csv("data/earthquakes.csv")
    assert_equals(3040, lesson7.problem_1(df))


def test_():
    df = pd.read_csv("data/earthquakes.csv")
    df_result = lesson7.problem_2(df)
    ids = ["us10006cwy", "us10006cx0", "us10006cxc", "us10006cxf"]
    ser = pd.Series(ids, index=[3877, 3897, 4012, 4036])
    ok = series_equals(df_result["id"], ser)
    assert_equals(ok, True)


def test_():
    df = pd.read_csv("data/earthquakes.csv")
    index = df["magnitude"].idxmax()
    expected = df.loc[index]
    actual = lesson7.problem_3(df)
    ok = series_equals(expected, actual)
    self.assertTrue(ok)


def test_():
    df = pd.read_csv("data/ufos.csv")
    ans = df.groupby("shape")["duration (seconds)"].mean()
    result = lesson8.problem_0(df)
    ok = series_equals(ans, result)
    self.assert_equals(ok, True)


def test_():
    df = pd.read_csv("data/ufos.csv")
    ans = (
        df[(df["latitude"] > 0) | (df["longitude"] > 0)]
        .groupby("city")["duration (seconds)"]
        .max()
    )
    result = lesson8.problem_1(df)
    ok = series_equals(ans, result)
    assert_equals(ok, True)


def test_():
    df = pd.read_csv("data/ufos.csv")
    ans = "birmingham (uk/england)"
    result = lesson8.problem_2(df)
    assert_equals(ans, result)


def test_():
    df = pd.read_csv("data/ufos.csv")
    vals = [24, 17, 6, 26, 25, 29, 26, 16, 20, 16]
    ser = pd.Series(vals)
    result = lesson8.problem_3(df)
    ok = series_equals(ser, result[0:10])
    assert_equals(ok, True)


def lesson9_prob1_test():
    # Enter code here
    ok = compare_plots("prob1.png", "test/prob1.png")
    assert_equals(ok, True)


def lesson9_prob2_test():
    ok = compare_plots("prob2.png", "test/prob2.png")
    assert_equals(ok, True)


def lesson9_prob3_test():
    # Enter code here
    ok = compare_plots("prob3.png", "test/prob3.png")
    assert_equals(ok, True)


def lesson9_prob4_test():
    # Enter code here
    ok = compare_plots("prob4.png", "test/prob4.png")
    assert_equals(ok, True)
