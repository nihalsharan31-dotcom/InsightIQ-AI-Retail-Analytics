import streamlit as st


def show_summary_cards(summary):

    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", summary["Rows"])

    col2.metric("Columns", summary["Columns"])

    col3.metric("Missing", summary["Missing Values"])

    col4, col5 = st.columns(2)

    col4.metric("Duplicates", summary["Duplicate Rows"])

    col5.metric(
        "Memory",
        f'{summary["Memory Usage (MB)"]} MB'
    )