import streamlit as st

from config import APP_NAME, APP_TITLE

st.set_page_config(
    page_title=APP_NAME,
    page_icon="📊",
    layout="wide"
)

st.title(APP_NAME)

st.caption(APP_TITLE)

st.info(
    "Use the sidebar to navigate to the Upload page."
)