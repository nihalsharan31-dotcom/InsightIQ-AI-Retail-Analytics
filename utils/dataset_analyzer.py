import pandas as pd


def dataset_summary(df):

    summary = {

        "Rows": df.shape[0],

        "Columns": df.shape[1],

        "Missing Values": int(df.isnull().sum().sum()),

        "Duplicate Rows": int(df.duplicated().sum()),

        "Memory Usage (MB)": round(
            df.memory_usage(deep=True).sum() / 1024 / 1024,
            2
        )

    }

    return summary