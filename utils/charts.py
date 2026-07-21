import plotly.express as px


def histogram(df, column):
    return px.histogram(
        df,
        x=column,
        title=f"Distribution of {column}"
    )


def box_plot(df, column):
    return px.box(
        df,
        y=column,
        title=f"Box Plot of {column}"
    )


def correlation_heatmap(df):
    numeric_df = df.select_dtypes(include="number")

    corr = numeric_df.corr(numeric_only=True)

    fig = px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        title="Correlation Heatmap"
    )

    return fig