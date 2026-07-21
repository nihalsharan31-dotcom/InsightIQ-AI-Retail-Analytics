import pandas as pd


def build_context(df: pd.DataFrame) -> str:
    """
    Build a compact summary of the uploaded dataset.
    This context will later be sent to the LLM.
    """

    context = []

    context.append(f"Rows: {len(df)}")
    context.append(f"Columns: {len(df.columns)}")

    if "Sales" in df.columns:
        context.append(
            f"Total Sales: {df['Sales'].sum():,.2f}"
        )

    if "Profit" in df.columns:
        context.append(
            f"Total Profit: {df['Profit'].sum():,.2f}"
        )

    if "Category" in df.columns and "Sales" in df.columns:
        category = (
            df.groupby("Category")["Sales"]
            .sum()
            .idxmax()
        )
        context.append(f"Top Category: {category}")

    if "Region" in df.columns and "Sales" in df.columns:
        region = (
            df.groupby("Region")["Sales"]
            .sum()
            .idxmax()
        )
        context.append(f"Top Region: {region}")

    missing = int(df.isnull().sum().sum())
    context.append(f"Missing Values: {missing}")

    return "\n".join(context)