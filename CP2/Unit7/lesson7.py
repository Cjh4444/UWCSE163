def problem_0(df):
    return df["magnitude"].mean()


def problem_1(df):
    return len(df[df["magnitude"] > problem_0(df)])


def problem_2(df):
    is_tonga = df["name"] == "Tonga"
    is_papua_new_guinea = df["name"] == "Papua New Guinea"
    tonga_papua_df = df[is_tonga | is_papua_new_guinea]

    is_8th_of_month = tonga_papua_df["day"] == 8

    return tonga_papua_df[is_8th_of_month]


def problem_3(df):
    max_idx = df["magnitude"].idxmax()

    return df.iloc[max_idx]
