import streamlit as st
import pandas as pd

st.title("📁 Dataset Upload")

uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

    else:
        df = pd.read_excel(uploaded_file)

    st.success("Dataset uploaded successfully!")

    st.subheader("Dataset Preview")

    st.dataframe(df)

    st.subheader("Dataset Information")

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", int(df.isnull().sum().sum()))

    st.subheader("Column Data Types")

    st.dataframe(df.dtypes.astype(str))