import geopandas as gpd
from geopandas import GeoDataFrame
import pandas as pd
import matplotlib.pyplot as plt


def load_in_data(washington_file: str, food_file: str) -> GeoDataFrame:
    washington_df = gpd.read_file(washington_file)
    food_df = pd.read_csv(food_file)

    merged: gpd.GeoDataFrame = washington_df.merge(
        food_df,
        left_on="CTIDFP00",
        right_on="CensusTract",
        how="left",
    )

    return merged


def percentage_food_data(gdf: GeoDataFrame) -> float:
    num_rows: int = gdf["CTIDFP00"].count()
    num_na: int = gdf["State"].isna().sum()

    return (num_rows - num_na) / num_rows * 100


def plot_map(gdf: GeoDataFrame):
    plot = gdf.plot()

    plt.title("Washington State")
    plt.savefig("map.png")


def main():
    state_data = load_in_data(
        "food_access/washington.json", "food_access/food_access.csv"
    )
    print(state_data.shape)
    print(percentage_food_data(state_data))
    plot_map(state_data)
    # plot_population_map(state_data)
    # plot_population_county_map(state_data)
    # plot_food_access_by_county(state_data)
    # plot_low_access_tracts(state_data)


if __name__ == "__main__":
    main()
