"""
Camden Harris
CSE 163 AX
Plot creation based on country data
"""

import os
import tempfile
import geopandas as gpd  # noqa: F401
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt  # noqa: F401

os.environ["MPLCONFIGDIR"] = tempfile.gettempdir()


def create_south_america_png():
    """
    Creates a heatmap plot of south america based on population
    """

    gdf: GeoDataFrame = gpd.read_file("geo_data/ne_110m_admin_0_countries.shp")
    important = gdf[["CONTINENT", "POP_EST", "geometry"]]

    is_south_america = important["CONTINENT"] == "South America"

    south_america = important[is_south_america]

    fig, ax = plt.subplots(1)

    south_america.plot(
        ax=ax,
        column="POP_EST",
        legend=True,
    )

    fig.savefig("south_america.png")

    pass


def create_small_and_rich_png():
    """
    Creates a heat map based on GDP of the
    simultaneously rich and small countries
    Rich: GDP of at least 500k
    Small: Population below 80M
    """
    gdf: GeoDataFrame = gpd.read_file("geo_data/ne_110m_admin_0_countries.shp")

    important = gdf[["CONTINENT", "POP_EST", "GDP_MD_EST", "geometry"]]

    is_rich = important["GDP_MD_EST"] >= 500000
    is_small = important["POP_EST"] <= 80000000

    rich_and_small = important[is_rich & is_small]

    fig, ax = plt.subplots(figsize=(15, 7))

    gdf.plot(ax=ax, color="#EEEEEE", figsize=(15, 7))

    rich_and_small.plot(
        ax=ax, column="GDP_MD_EST", legend=True, figsize=(15, 7)
    )

    fig.savefig("small_and_rich.png")
    pass


def create_populations_png():
    """
    Creates a 3 plots of world
    Plot 1: Heatmap based on population of country
    Plot 2: Heatmap based on population of subregion
    Plot 3: Heatmap based on population of continent
    """

    gdf: GeoDataFrame = gpd.read_file("geo_data/ne_110m_admin_0_countries.shp")

    important: GeoDataFrame = gdf[
        ["CONTINENT", "SUBREGION", "POP_EST", "geometry"]
    ]

    fig, [ax1, ax2, ax3] = plt.subplots(nrows=3)

    important.plot(ax=ax1, column="POP_EST", legend=True)

    sub_regions = important.dissolve(by="SUBREGION", aggfunc="sum")
    sub_regions.plot(ax=ax2, column="POP_EST", legend=True)

    continents = important.dissolve(by="CONTINENT", aggfunc="sum")
    continents.plot(ax=ax3, column="POP_EST", legend=True)

    fig.savefig("populations.png")
    pass


def main():
    create_south_america_png()
    create_small_and_rich_png()
    create_populations_png()


if __name__ == "__main__":
    main()
