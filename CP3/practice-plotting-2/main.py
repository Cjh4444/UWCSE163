import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()


def main():
    # Read iris_missing.csv file using pandas library
    df = pd.read_csv("CP3/practice-plotting-2/iris_missing.csv").fillna(0)

    sns.regplot(data=df, x="petal_length", y="sepal_length", color="g")

    # Save the plot to a file
    # For this problem, we need an extra parameter for a better layout.
    plt.title("Petal Length vs Sepal Length")
    plt.xlabel("Petal Length (cm)")
    plt.ylabel("Sepal Length (cm)")
    plt.savefig("CP3/practice-plotting-2/plot.png", bbox_inches="tight")


if __name__ == "__main__":
    main()
