import pandas as pd


def apply_filters(df, region, category, segment):

    filtered_df = df.copy()

    if region != "All":
        filtered_df = filtered_df[
            filtered_df["Region"] == region
        ]

    if category != "All":
        filtered_df = filtered_df[
            filtered_df["Category"] == category
        ]

    if segment != "All":
        filtered_df = filtered_df[
            filtered_df["Segment"] == segment
        ]

    return filtered_df