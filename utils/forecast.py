import pandas as pd


def prepare_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare daily sales data for forecasting.

    Returns
    -------
    DataFrame
        Columns:
        - ds : Date
        - y  : Daily Sales
    """

    data = df.copy()

    # Convert Order Date to datetime
    data["Order Date"] = pd.to_datetime(
    data["Order Date"],
    format="%m/%d/%Y",
    errors="coerce"
    )

    # Remove invalid dates
    data = data.dropna(subset=["Order Date"])

    # Group sales by day
    daily_sales = (
        data.groupby("Order Date")["Sales"]
        .sum()
        .reset_index()
    )

    # Rename columns for forecasting
    daily_sales.columns = ["ds", "y"]

    # Sort by date
    daily_sales = daily_sales.sort_values("ds")

    return daily_sales