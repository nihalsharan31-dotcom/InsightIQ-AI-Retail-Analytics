import plotly.express as px
import pandas as pd


def create_histogram(df: pd.DataFrame, column: str):
    """Create histogram for a numeric column."""
    return px.histogram(
        df,
        x=column,
        title=f"Distribution of {column}",
        nbins=30,
    )


def create_box_plot(df: pd.DataFrame, column: str):
    """Create box plot for a numeric column."""
    return px.box(
        df,
        y=column,
        title=f"Box Plot of {column}",
    )