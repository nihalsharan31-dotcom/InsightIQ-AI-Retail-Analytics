import streamlit as st
from config import APP_NAME, APP_TAGLINE

st.set_page_config(
    page_title=APP_NAME,
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title(APP_NAME)

st.caption(APP_TAGLINE)

st.success("Welcome to InsightIQ!")

st.info(
    "Select a module from the sidebar to begin your analytics journey."
)