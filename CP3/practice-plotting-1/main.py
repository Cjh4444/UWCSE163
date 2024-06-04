import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()


def main():
    # Read iris.csv file using pandas library
    df = pd.read_csv("CP3/practice-plotting-1/iris.csv")

    sns.relplot(data=df, x="petal_width", y="petal_length", hue="species")

    # Save the plot to a file
    # For this problem, we need an extra parameter for a better layout.
    plt.title("Petal Width vs Length")
    plt.xlabel("Petal Width (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.savefig("CP3/practice-plotting-1/plot.png", bbox_inches="tight")


if __name__ == "__main__":
    main()
