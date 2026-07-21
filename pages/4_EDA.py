import streamlit as st

from utils.session_manager import (
    has_dataset,
    get_dataset
)

from utils.charts import (
    histogram,
    box_plot,
    correlation_heatmap
)

st.title("📊 Exploratory Data Analysis")

if not has_dataset():
    st.warning("Please upload a dataset first.")
    st.stop()

df = get_dataset()

st.success("Dataset Loaded")

st.subheader("Dataset Shape")

col1, col2 = st.columns(2)

col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])

st.divider()

st.subheader("Statistical Summary")

st.dataframe(df.describe())

numeric_columns = list(
    df.select_dtypes(include="number").columns
)

if numeric_columns:

    selected_column = st.selectbox(
        "Select Numeric Column",
        numeric_columns
    )

    st.plotly_chart(
        histogram(df, selected_column),
        use_container_width=True
    )

    st.plotly_chart(
        box_plot(df, selected_column),
        use_container_width=True
    )

    st.plotly_chart(
        correlation_heatmap(df),
        use_container_width=True
    )

else:

    st.info("No numeric columns found.")