import streamlit as st

from utils.cleaner import (
    remove_duplicates,
    drop_missing,
    fill_missing_mean,
    fill_missing_median,
    fill_missing_mode,
)

from utils.session_manager import get_dataset, has_dataset, set_dataset

st.title("🧹 Data Cleaning")

# Check if a dataset has been uploaded
if not has_dataset():
    st.warning("Please upload a dataset first.")
    st.stop()

# Get dataset from session
df = get_dataset()

st.success("Dataset Loaded Successfully")

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

    set_dataset(cleaned_df) 
    st.success("Cleaning completed successfully!")

    st.subheader("Cleaned Dataset Preview")
    st.dataframe(cleaned_df.head(20), use_container_width=True)

    csv = cleaned_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download Cleaned Dataset",
        data=csv,
        file_name="cleaned_dataset.csv",
        mime="text/csv",
    )