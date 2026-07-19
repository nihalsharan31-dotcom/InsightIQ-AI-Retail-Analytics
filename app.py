import streamlit as st

st.set_page_config(
    page_title="InsightIQ",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 InsightIQ")
st.subheader("AI-Powered Retail & Sales Analytics Platform")

st.markdown("""
Welcome to **InsightIQ**.

This platform helps businesses:
- 📁 Upload sales datasets
- 🧹 Clean messy data
- 📊 Generate interactive dashboards
- 🤖 Produce AI-powered business insights
- 📈 Forecast future sales
- 📄 Export reports
""")

st.info("👈 Use the sidebar to navigate through the application.")