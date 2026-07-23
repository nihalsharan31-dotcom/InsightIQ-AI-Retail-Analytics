from pathlib import Path
import streamlit as st


def load_theme():
    css_path = Path("assets/css/main.css")
    anim_path = Path("assets/css/animations.css")

    css = css_path.read_text(encoding="utf-8")
    anim = anim_path.read_text(encoding="utf-8")

    st.markdown(
        f"<style>{css}{anim}</style>",
        unsafe_allow_html=True
    )