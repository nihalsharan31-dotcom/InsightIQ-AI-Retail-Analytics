import streamlit as st

from config import SUPPORTED_FILE_TYPES

from utils.file_handler import load_dataset

from utils.validators import validate_file

from utils.profiler import profile_dataset

st.title("📂 Dataset Upload")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel",
    type=SUPPORTED_FILE_TYPES
)

if uploaded_file:

    valid, message = validate_file(uploaded_file)

    if not valid:
        st.error(message)
        st.stop()

    try:

        dataframe = load_dataset(uploaded_file)

        st.success("Dataset uploaded successfully!")

        profile = profile_dataset(dataframe)

        col1, col2, col3 = st.columns(3)

        col1.metric("Rows", profile["Rows"])
        col2.metric("Columns", profile["Columns"])
        col3.metric("Missing", profile["Missing Values"])

        col4, col5, col6 = st.columns(3)

        col4.metric("Duplicates", profile["Duplicate Rows"])
        col5.metric("Memory", f'{profile["Memory (MB)"]} MB')
        col6.metric("Numeric", profile["Numeric Columns"])

        st.divider()

        st.subheader("Dataset Preview")

        st.dataframe(dataframe.head(20), use_container_width=True)

        st.subheader("Column Data Types")

        st.dataframe(
            dataframe.dtypes.astype(str).rename("Data Type")
        )

    except Exception as e:

        st.error(str(e))