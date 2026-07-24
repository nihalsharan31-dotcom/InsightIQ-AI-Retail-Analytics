import streamlit as st

def require_dataset():
    """Redirect user to Upload page if no dataset is loaded."""
    if "dataset" not in st.session_state or st.session_state["dataset"] is None:
        st.warning("⚠ Please upload a dataset first.")
        st.switch_page("pages/2_Upload.py")
        st.stop()