import streamlit as st

from utils.session_manager import (
    has_dataset,
    get_dataset,
)

from utils.charts import (
    create_histogram,
    create_box_plot,
)

st.title("📊 Exploratory Data Analysis")

# Check whether a dataset exists
if not has_dataset():
    st.warning("Please upload a dataset first.")
    st.stop()

# Load dataset from session
df = get_dataset()

st.success("Dataset loaded successfully!")

# --------------------------------------------------
# Dataset Overview
# --------------------------------------------------

st.header("Dataset Overview")

col1, col2 = st.columns(2)

col1.metric("Rows", df.shape[0])
col2.metric("Columns", df.shape[1])

# --------------------------------------------------
# Statistical Summary
# --------------------------------------------------

st.header("Statistical Summary")

st.dataframe(
    df.describe(),
    use_container_width=True,
)

# --------------------------------------------------
# Charts
# --------------------------------------------------

numeric_columns = list(
    df.select_dtypes(include="number").columns
)

if not numeric_columns:
    st.info("No numeric columns available.")
    st.stop()

selected_column = st.selectbox(
    "Select Numeric Column",
    numeric_columns,
)

st.plotly_chart(
    create_histogram(df, selected_column),
    use_container_width=True,
)

st.plotly_chart(
    create_box_plot(df, selected_column),
    use_container_width=True,
)