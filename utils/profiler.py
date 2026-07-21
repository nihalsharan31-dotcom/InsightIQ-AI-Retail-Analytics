import pandas as pd


def profile_dataset(df: pd.DataFrame):

    numeric_columns = len(
        df.select_dtypes(include="number").columns
    )

    categorical_columns = len(
        df.select_dtypes(include="object").columns
    )

    datetime_columns = len(
        df.select_dtypes(include="datetime").columns
    )

    summary = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Rows": int(df.duplicated().sum()),
        "Memory (MB)": round(
            df.memory_usage(deep=True).sum() / 1024 / 1024,
            2
        ),
        "Numeric Columns": numeric_columns,
        "Categorical Columns": categorical_columns,
        "Datetime Columns": datetime_columns,
    }

    return summary