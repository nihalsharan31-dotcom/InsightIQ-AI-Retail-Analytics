import streamlit as st
from theme import load_theme
from config import APP_NAME, APP_TITLE

st.set_page_config(
    page_title=APP_NAME,
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_theme()

st.title(APP_NAME)

st.caption(APP_TITLE)

st.info(
    "Select a page from the sidebar to get started."
)