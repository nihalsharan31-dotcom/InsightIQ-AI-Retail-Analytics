import streamlit as st

from config import APP_NAME, APP_TITLE
from utils.ui import (
    load_custom_css,
    page_title,
)

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Home",
    layout="wide"
)

load_custom_css()

# --------------------------------------------------
# Header
# --------------------------------------------------

page_title(
    f"🚀 {APP_NAME}",
    APP_TITLE
)

st.markdown(
    """
Welcome to **InsightIQ**, an AI-Powered Retail Analytics Platform designed to help
businesses transform raw sales data into meaningful insights, interactive dashboards,
AI-generated recommendations, forecasting, and executive reports.
"""
)

st.divider()

# --------------------------------------------------
# Platform Features
# --------------------------------------------------

st.subheader("✨ Platform Features")

col1, col2 = st.columns(2)

with col1:
    st.success("📁 Upload Retail Dataset")
    st.success("🧹 Clean & Validate Data")
    st.success("📊 Interactive Dashboard")
    st.success("📈 Sales Analytics")

with col2:
    st.success("🤖 AI Business Insights")
    st.success("🔮 Sales Forecasting")
    st.success("📄 Executive PDF Reports")
    st.success("⚙️ Intelligent Data Profiling")

st.divider()

# --------------------------------------------------
# Workflow
# --------------------------------------------------

st.subheader("🔄 Analytics Workflow")

st.markdown("""
1. 📁 Upload a retail dataset
2. 🧹 Clean and validate the data
3. 📊 Explore interactive visualizations
4. 🤖 Generate AI-powered business insights
5. 📈 Forecast future sales
6. 📄 Download executive PDF reports
""")

st.divider()

# --------------------------------------------------
# Technologies
# --------------------------------------------------

st.subheader("🛠️ Technology Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

tech1.info("🐍 Python")
tech2.info("📊 Streamlit")
tech3.info("🤖 OpenRouter AI")
tech4.info("📈 Plotly")

st.divider()

# --------------------------------------------------
# Quick Start
# --------------------------------------------------

st.subheader("🚀 Get Started")

st.info(
    "Navigate to the **Upload** page from the sidebar and upload a retail dataset to begin your analytics journey."
)

st.success("🎉 Welcome to InsightIQ! Your AI-powered business analytics platform is ready.")