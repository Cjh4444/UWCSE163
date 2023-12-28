def problem_0(df):
    return df.groupby("shape")["duration (seconds)"].mean()


def problem_1(df):
    positive_lat = df["latitude"] > 0
    positive_long = df["longitude"] > 0

    return (
        df[positive_lat | positive_long]
        .groupby("city")["duration (seconds)"]
        .max()
    )


def problem_2(df):
    return df.groupby("city")["duration (seconds)"].max().idxmax()


def problem_3(df):
    def comment_word_length(str):
        return len(str.split())

    return df["comments"].apply(comment_word_length)
