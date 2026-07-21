import pandas as pd


def remove_duplicates(df: pd.DataFrame):
    """
    Remove duplicate rows.
    """
    return df.drop_duplicates()


def drop_missing(df: pd.DataFrame):
    """
    Remove rows containing missing values.
    """
    return df.dropna()


def fill_missing_mean(df: pd.DataFrame):
    """
    Fill missing numeric values using the mean.
    """
    cleaned_df = df.copy()

    numeric_cols = cleaned_df.select_dtypes(include="number").columns

    for col in numeric_cols:
        cleaned_df[col] = cleaned_df[col].fillna(cleaned_df[col].mean())

    return cleaned_df


def fill_missing_median(df: pd.DataFrame):
    """
    Fill missing numeric values using the median.
    """
    cleaned_df = df.copy()

    numeric_cols = cleaned_df.select_dtypes(include="number").columns

    for col in numeric_cols:
        cleaned_df[col] = cleaned_df[col].fillna(cleaned_df[col].median())

    return cleaned_df


def fill_missing_mode(df: pd.DataFrame):
    """
    Fill missing values using the mode.
    Works for both numeric and categorical columns.
    """
    cleaned_df = df.copy()

    for col in cleaned_df.columns:
        mode = cleaned_df[col].mode()

        if not mode.empty:
            cleaned_df[col] = cleaned_df[col].fillna(mode[0])

    return cleaned_df