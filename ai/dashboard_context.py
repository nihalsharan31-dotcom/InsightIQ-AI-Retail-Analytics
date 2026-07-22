import pandas as pd


def build_dashboard_context(df: pd.DataFrame) -> str:
    """
    Build dashboard context for AI explanation.
    """

    context = []

    context.append(f"Total Rows: {len(df):,}")
    context.append(f"Columns: {len(df.columns)}")

    if "Sales" in df.columns:
        context.append(
            f"Total Sales: ${df['Sales'].sum():,.2f}"
        )
        context.append(
            f"Average Sales: ${df['Sales'].mean():,.2f}"
        )

    if "Profit" in df.columns:
        context.append(
            f"Total Profit: ${df['Profit'].sum():,.2f}"
        )
        context.append(
            f"Average Profit: ${df['Profit'].mean():,.2f}"
        )

    if "Category" in df.columns and "Sales" in df.columns:
        category = (
            df.groupby("Category")["Sales"]
            .sum()
            .idxmax()
        )

        context.append(
            f"Top Category: {category}"
        )

    if "Region" in df.columns and "Sales" in df.columns:
        region = (
            df.groupby("Region")["Sales"]
            .sum()
            .idxmax()
        )

        context.append(
            f"Top Region: {region}"
        )

    context.append(
        f"Missing Values: {df.isna().sum().sum()}"
    )

    context.append(
        f"Duplicate Rows: {df.duplicated().sum()}"
    )

    return "\n".join(context)