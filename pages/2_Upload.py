import streamlit as st

from utils.file_handler import load_dataset

from utils.dataset_analyzer import dataset_summary

from utils.ui_components import show_summary_cards


st.title("📂 Dataset Upload")

uploaded_file = st.file_uploader(

    "Upload CSV or Excel",

    type=["csv", "xlsx"]

)

if uploaded_file:

    df = load_dataset(uploaded_file)

    st.success("Dataset Uploaded Successfully!")

    summary = dataset_summary(df)

    show_summary_cards(summary)

    st.subheader("Dataset Preview")

    st.dataframe(df.head(20))

    st.subheader("Column Information")

    st.dataframe(df.dtypes.astype(str))