from pathlib import Path
import streamlit as st


def load_custom_css():
    """Load global CSS styling."""

    css_path = Path("assets/css/main.css")

    if css_path.exists():
        with open(css_path, encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

def page_title(title: str, subtitle: str = ""):
    """Display a consistent page title."""

    st.title(title)

    if subtitle:
        st.caption(subtitle)

    st.divider()


def section_header(title: str):
    """Display a consistent section header."""

    st.subheader(title)


def info_banner(message: str):
    """Display an informational banner."""

    st.info(message)