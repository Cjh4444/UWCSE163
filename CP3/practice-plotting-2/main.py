import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set()


def main():
    # Read iris_missing.csv file using pandas library
    df = pd.read_csv("CP3/practice-plotting-2/iris_missing.csv").fillna(0)

    graph = sns.regplot(data=df, x="petal_length", y="sepal_length", color="g")

    graph.set_title("Petal Length vs Sepal Length")
    graph.set_xlabel("Petal Length (cm)")
    graph.set_ylabel("Sepal Length (cm)")

    # Save the plot to a file
    # For this problem, we need an extra parameter for a better layout.
    plt.savefig("CP3/practice-plotting-2/plot.png", bbox_inches="tight")


if __name__ == "__main__":
    main()
