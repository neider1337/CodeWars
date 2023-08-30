import pandas as pd


def max_common(df_a, df_b):
    df2_a = df_a.copy()
    df2_b = df_b.copy()
    cols = df2_a.columns.intersection(df2_b.columns)
    new_data = {}

    for column in df2_a.columns:
        if column in cols:
            new_data[column] = df2_a[column].combine(df_b[column], max)
        else:
            new_data[column] = df2_a[column]
    return pd.DataFrame(new_data, index=df2_a.index)