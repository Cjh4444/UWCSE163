"""
Camden Harris
CSE 163 AX
This program implements the functions for HW5 that create various plots
"""

import geopandas as gpd
from geopandas import GeoDataFrame
import pandas as pd
import matplotlib.pyplot as plt


def load_in_data(washington_file: str, food_file: str) -> GeoDataFrame:
    """
    Merges the food access data and the geographical data
    Keyword arguments:
    washington_file - geographical data of washington
    food_file - food access data for thousands of tracts.
    """
    washington_df = gpd.read_file(washington_file)
    food_df = pd.read_csv(food_file, index_col=0)

    merged: gpd.GeoDataFrame = washington_df.merge(
        food_df,
        left_on="CTIDFP00",
        right_on="CensusTract",
        how="left",
    )

    return merged


def percentage_food_data(gdf: GeoDataFrame) -> float:
    """
    Returns the percentage of tracts in Washington with data
    Keyword arguments:
    gdf - geo dataframe of washington tracts with food data
    """
    num_rows: int = gdf["CTIDFP00"].count()
    num_na: int = gdf["State"].isna().sum()

    return (num_rows - num_na) / num_rows * 100


def plot_map(gdf: GeoDataFrame) -> None:
    """
    Plots the shapes of tracts in washington
    Keyword arguments:
    gdf - geo dataframe of washington tracts with food data
    """
    fig, ax = plt.subplots(1)

    gdf.plot(ax=ax)

    plt.title("Washington State")
    plt.savefig("map.png")


def plot_population_map(gdf: GeoDataFrame) -> None:
    """
    Plots a heatmap of the tracts in Washington based on population
    Keyword arguments:
    gdf - geo dataframe of washington tracts with food data
    """
    important_data = gdf[["CensusTract", "POP2010", "geometry"]]

    fig, ax = plt.subplots(1)

    important_data.plot(ax=ax, color="#EEEEEE")

    gdf.plot(
        ax=ax,
        column="POP2010",
        legend=True,
    )

    plt.title("Washington Census Tract Population")
    plt.savefig("population_map.png")


def plot_population_county_map(gdf: GeoDataFrame) -> None:
    """
    Plots a heatmap of the counties in Washington based on population
    Keyword arguments:
    gdf - geo dataframe of washington tracts with food data
    """
    important_data: GeoDataFrame = gdf[
        ["CensusTract", "County", "POP2010", "geometry"]
    ]

    fig, ax = plt.subplots(1)

    important_data.plot(ax=ax, color="#EEEEEE")

    counties = important_data.dissolve(by="County", aggfunc="sum")

    counties.plot(ax=ax, column="POP2010", legend=True)

    plt.title("Washington County Populations")
    plt.savefig("county_population_map.png")


def plot_food_access_by_county(gdf: GeoDataFrame) -> None:
    """
    Plots a heatmap of the counties in Washington based on ratio of low income
    population to food access
    Keyword arguments:
    gdf - geo dataframe of washington tracts with food data
    """
    important_data: GeoDataFrame = gdf[
        [
            "County",
            "geometry",
            "POP2010",
            "lapophalf",
            "lapop10",
            "lalowihalf",
            "lalowi10",
        ]
    ]

    counties: GeoDataFrame = important_data.dissolve(
        by="County", aggfunc="sum"
    )

    counties["lapophalf_ratio"] = counties["lapophalf"] / counties["POP2010"]
    counties["lapop10_ratio"] = counties["lapop10"] / counties["POP2010"]
    counties["lalowihalf_ratio"] = counties["lalowihalf"] / counties["POP2010"]
    counties["lalowi10_ratio"] = counties["lalowi10"] / counties["POP2010"]

    fig, [[ax1, ax2], [ax3, ax4]] = plt.subplots(2, 2, figsize=(20, 10))

    important_data[important_data["POP2010"].isna()].plot(
        color="#EEEEEE", ax=ax1
    )
    important_data[important_data["POP2010"].isna()].plot(
        color="#EEEEEE", ax=ax2
    )
    important_data[important_data["POP2010"].isna()].plot(
        color="#EEEEEE", ax=ax3
    )
    important_data[important_data["POP2010"].isna()].plot(
        color="#EEEEEE", ax=ax4
    )

    counties.plot(
        ax=ax1, column="lapophalf_ratio", legend=True, vmin=0, vmax=1
    )
    ax1.set_title("Low Access: Half")

    counties.plot(
        ax=ax2, column="lalowihalf_ratio", legend=True, vmin=0, vmax=1
    )
    ax2.set_title("Low Access + Low Income: Half")

    counties.plot(ax=ax3, column="lapop10_ratio", legend=True, vmin=0, vmax=1)
    ax3.set_title("Low Access: 10")

    counties.plot(ax=ax4, column="lalowi10_ratio", legend=True, vmin=0, vmax=1)
    ax4.set_title("Low Access + Low Income: 10")

    plt.savefig("county_food_access.png")


def plot_low_access_tracts(gdf: GeoDataFrame) -> None:
    """
    Plots a highlighted map of all tracts that are considered low access
    Keyword arguments:
    gdf - geo dataframe of washington tracts with food data
    """
    important_data: GeoDataFrame = gdf[
        ["Urban", "Rural", "POP2010", "lapophalf", "lapop10", "geometry"]
    ]

    is_urban = important_data["Urban"] == 1

    urban_la_500 = important_data["lapophalf"] >= 500
    urban_la_33_percent = important_data["lapophalf"] / important_data[
        "POP2010"
    ] >= (1 / 3)
    urban_la = is_urban & (urban_la_500 | urban_la_33_percent)

    is_rural = important_data["Rural"] == 1
    rural_la_500 = important_data["lapop10"] >= 500
    rural_la_33_percent = important_data["lapop10"] / important_data[
        "POP2010"
    ] >= (1 / 3)
    rural_la = is_rural & (rural_la_500 | rural_la_33_percent)

    general_la = urban_la | rural_la

    fig, ax = plt.subplots(1)
    important_data.plot(ax=ax, color="#EEEEEE")
    important_data.dropna().plot(ax=ax, color="#AAAAAA")
    important_data[general_la].plot(ax=ax)

    plt.title("Low Access Census Tracts")
    plt.savefig("low_access.png")


def main():
    """
    Runs all the functions in this file to create the plots
    """
    state_data = load_in_data(
        "food_access/washington.json", "food_access/food_access.csv"
    )
    print(state_data.shape)
    print(percentage_food_data(state_data))
    plot_map(state_data)
    plot_population_map(state_data)
    plot_population_county_map(state_data)
    plot_food_access_by_county(state_data)
    plot_low_access_tracts(state_data)


if __name__ == "__main__":
    main()
