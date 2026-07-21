import pandas as pd


def generate_executive_summary(df: pd.DataFrame) -> str:
    """
    Generate a business summary of the uploaded dataset.
    """

    rows = len(df)
    columns = len(df.columns)

    summary = []

    summary.append(
        f"The uploaded dataset contains {rows:,} records and {columns} columns."
    )

    # Sales
    if "Sales" in df.columns:
        total_sales = df["Sales"].sum()
        average_sales = df["Sales"].mean()

        summary.append(
            f"Total sales are ${total_sales:,.2f} with an average order value of ${average_sales:,.2f}."
        )

    # Profit
    if "Profit" in df.columns:
        total_profit = df["Profit"].sum()

        summary.append(
            f"Overall profit is ${total_profit:,.2f}."
        )

    # Best Category
    if "Category" in df.columns and "Sales" in df.columns:

        best_category = (
            df.groupby("Category")["Sales"]
            .sum()
            .idxmax()
        )

        summary.append(
            f"The highest-selling category is {best_category}."
        )

    # Best Region
    if "Region" in df.columns and "Sales" in df.columns:

        best_region = (
            df.groupby("Region")["Sales"]
            .sum()
            .idxmax()
        )

        summary.append(
            f"The best-performing region is {best_region}."
        )

    # Missing Values
    missing = int(df.isnull().sum().sum())

    if missing == 0:
        summary.append(
            "No missing values were detected in the dataset."
        )
    else:
        summary.append(
            f"The dataset contains {missing} missing values that should be reviewed."
        )

    return " ".join(summary)