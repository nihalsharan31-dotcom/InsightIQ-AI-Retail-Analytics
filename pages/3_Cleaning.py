import streamlit as st
import pandas as pd

from utils.cleaner import (
    remove_duplicates,
    drop_missing,
    fill_missing_mean,
    fill_missing_median,
    fill_missing_mode,
)

st.title("🧹 Data Cleaning")

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv", "xlsx"]
)

if uploaded_file:

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("Dataset Loaded")

    cleaning_option = st.selectbox(
        "Select Cleaning Method",
        [
            "Remove Duplicate Rows",
            "Drop Missing Rows",
            "Fill Missing (Mean)",
            "Fill Missing (Median)",
            "Fill Missing (Mode)"
        ]
    )

    if st.button("Clean Dataset"):

        if cleaning_option == "Remove Duplicate Rows":
            cleaned_df = remove_duplicates(df)

        elif cleaning_option == "Drop Missing Rows":
            cleaned_df = drop_missing(df)

        elif cleaning_option == "Fill Missing (Mean)":
            cleaned_df = fill_missing_mean(df)

        elif cleaning_option == "Fill Missing (Median)":
            cleaned_df = fill_missing_median(df)

        else:
            cleaned_df = fill_missing_mode(df)

        st.success("Cleaning completed successfully!")

        st.write("### Cleaned Dataset Preview")

        st.dataframe(cleaned_df.head(20), use_container_width=True)

        csv = cleaned_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "⬇ Download Cleaned Dataset",
            data=csv,
            file_name="cleaned_dataset.csv",
            mime="text/csv"
        )