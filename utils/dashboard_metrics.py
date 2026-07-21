import pandas as pd


def calculate_kpis(df: pd.DataFrame):
    """
    Calculate key business metrics from the dataset.
    """

    metrics = {}

    # Total Orders
    metrics["orders"] = len(df)

    # Total Sales
    if "Sales" in df.columns:
        metrics["sales"] = round(df["Sales"].sum(), 2)
        metrics["average_sales"] = round(df["Sales"].mean(), 2)
    else:
        metrics["sales"] = 0
        metrics["average_sales"] = 0

    # Total Profit
    if "Profit" in df.columns:
        metrics["profit"] = round(df["Profit"].sum(), 2)
    else:
        metrics["profit"] = 0

    return metrics