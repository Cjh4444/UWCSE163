import os
import tempfile
os.environ["MPLCONFIGDIR"] = tempfile.gettempdir()

import geopandas as gpd           # noqa: F401
import matplotlib.pyplot as plt   # noqa: F401


def create_south_america_png():
    pass
  
 
def create_small_and_rich_png():
    # Your code goes here!
    pass


def create_populations_png():
    # Your code goes here!
    pass


def main():
    create_south_america_png()
    create_small_and_rich_png()
    create_populations_png()


if __name__ == '__main__':
    main()