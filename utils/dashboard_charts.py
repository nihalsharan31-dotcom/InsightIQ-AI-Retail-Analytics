import plotly.express as px


def sales_by_category(df):

    chart = (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
    )

    return px.bar(
        chart,
        x="Category",
        y="Sales",
        title="Sales by Category"
    )


def sales_by_region(df):

    chart = (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
    )

    return px.pie(
        chart,
        names="Region",
        values="Sales",
        title="Sales by Region"
    )


def top_products(df):

    chart = (
        df.groupby("Product Name")["Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    return px.bar(
        chart,
        x="Sales",
        y="Product Name",
        orientation="h",
        title="Top 10 Products"
    )