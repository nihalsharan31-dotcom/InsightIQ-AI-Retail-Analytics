import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing


def prepare_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare daily sales data for forecasting.
    """

    data = df.copy()

    data["Order Date"] = pd.to_datetime(
        data["Order Date"],
        format="%m/%d/%Y",
        errors="coerce"
    )

    data = data.dropna(subset=["Order Date"])

    daily_sales = (
        data.groupby("Order Date")["Sales"]
        .sum()
        .reset_index()
    )

    daily_sales.columns = ["ds", "y"]

    daily_sales = daily_sales.sort_values("ds")

    return daily_sales


def forecast_sales(
    sales_data: pd.DataFrame,
    periods: int = 30
    ) -> pd.DataFrame:
    """
    Forecast future sales.
    """

    ts = sales_data.copy().set_index("ds")

    model = ExponentialSmoothing(
        ts["y"],
        trend="add",
        seasonal=None
    )

    fitted = model.fit(optimized=True)

    forecast = fitted.forecast(periods)

    future_dates = pd.date_range(
        start=ts.index.max() + pd.Timedelta(days=1),
        periods=periods,
        freq="D"
    )

    forecast_df = pd.DataFrame({
        "ds": future_dates,
        "Forecast": forecast.values
    })

    return forecast_df