import streamlit as st

def require_dataset():
    """Redirect user to Upload page if no dataset is loaded."""
    if "df" not in st.session_state or st.session_state.df is None:
        st.warning("⚠ Please upload a dataset first.")
        st.switch_page("pages/2_Upload.py")
        st.stop()