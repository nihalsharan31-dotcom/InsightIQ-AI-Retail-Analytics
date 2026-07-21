import streamlit as st

from utils.session_manager import (
    get_dataset,
    has_dataset,
)

from utils.summary_engine import (
    generate_executive_summary,
)

st.title("🤖 AI Business Analyst")

if not has_dataset():
    st.warning("Please upload a dataset first.")
    st.stop()

df = get_dataset()

st.subheader("📋 Executive Summary")

summary = generate_executive_summary(df)

st.info(summary)