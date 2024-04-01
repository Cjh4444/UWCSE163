"""
Your name
class
file description
"""

import os
import tempfile
import pandas as pd
from pandas import DataFrame, Series
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error


os.environ["MPLCONFIGDIR"] = tempfile.gettempdir()

# Your imports here


# Define your functions here
def compare_bachelors_1980(data: DataFrame) -> DataFrame:
    is_1980 = data["Year"] == 1980
    not_A = data["Sex"] != "A"

    df = data[is_1980 & not_A][["Sex", "Total"]]

    return df.groupby("Sex")["Total"].sum().reset_index()


def top_2_2000s(data: DataFrame, sex: str = "A") -> Series:
    is_after_2000 = 2000 <= data["Year"]
    is_before_2010 = data["Year"] <= 2010
    is_sex = data["Sex"] == sex

    df = data[is_after_2000 & is_before_2010 & is_sex]
    series = df.groupby("Min degree")["Total"].mean().nlargest(2)

    return series


def line_plot_bachelors(data: DataFrame):
    is_A = data["Sex"] == "A"
    is_bachelors = data["Min degree"] == "bachelor's"

    df = data[is_A & is_bachelors].dropna(subset=["Total"])

    sns.relplot(data=df, x="Year", y="Total", kind="line")

    plt.title("Percentage Earning Bachelor's over Time")
    plt.xlabel("Year")
    plt.ylabel("Percentage")
    plt.savefig("HW3/line_plot_bachelors.png", bbox_inches="tight")


def bar_chart_high_school(data: DataFrame):
    is_2009 = data["Year"] == 2009
    has_high_school = data["Min degree"] == "high school"

    df = data[is_2009 & has_high_school]

    sns.catplot(data=df, x="Sex", y="Total", kind="bar", hue="Sex")

    plt.title("Percentage Completed High School by Sex")
    plt.xlabel("Sex")
    plt.ylabel("Percentage")
    plt.savefig("HW3/bar_chart_high_school.png", bbox_inches="tight")


def plot_hispanic_min_degree(data: DataFrame):
    is_after_1990 = 1990 <= data["Year"]
    is_before_2010 = data["Year"] <= 2010
    has_high_school = data["Min degree"] == "high school"
    has_bachelors = data["Min degree"] == "bachelor's"

    df = data[
        is_after_1990 & is_before_2010 & (has_high_school | has_bachelors)
    ]

    df = df.groupby(["Year", "Min degree"])["Hispanic"].mean().to_frame()

    sns.catplot(data=df, x="Year", y="Hispanic", kind="bar", hue="Min degree")

    plt.title("Percentage of Hispanic People Earning Degrees over Time")
    plt.xlabel("Year")
    plt.ylabel("Percentage")
    plt.savefig("HW3/plot_hispanic_min_degree.png", bbox_inches="tight")


def fit_and_predict_degrees(data: DataFrame):
    data = data[["Year", "Min degree", "Sex", "Total"]].dropna()

    features = pd.get_dummies(data.loc[:, data.columns != "Total"])
    labels = data["Total"]

    features_train, features_test, labels_train, labels_test = (
        train_test_split(features, labels, test_size=0.2)
    )

    model = DecisionTreeRegressor()

    model.fit(features_train, labels_train)

    print(mean_squared_error(model.predict(features_train), labels_train))
    mse = mean_squared_error(model.predict(features_test), labels_test)

    print(mse)

    return mse


def main():
    data = pd.read_csv("HW3/nces-ed-attainment.csv", na_values=["---"])
    sns.set()
    # Call your functions here
    # print(compare_bachelors_1980(data))
    # print(top_2_2000s(data))
    # line_plot_bachelors(data)
    # bar_chart_high_school(data)
    # plot_hispanic_min_degree(data)
    fit_and_predict_degrees(data)


if __name__ == "__main__":
    main()
