import streamlit as st
from config import APP_NAME, APP_TAGLINE

st.set_page_config(page_title="Home", layout="wide")

# -----------------------------
# Header
# -----------------------------
st.title(f"📊 {APP_NAME}")
st.caption(APP_TAGLINE)

st.divider()

# -----------------------------
# KPI Cards
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Revenue", "₹0")
col2.metric("Profit", "₹0")
col3.metric("Orders", "0")
col4.metric("Customers", "0")

st.divider()

# -----------------------------
# About
# -----------------------------
st.subheader("🚀 About InsightIQ")

st.write("""
InsightIQ is an AI-Powered Retail Analytics Platform that helps businesses transform raw sales data into meaningful insights.

The platform provides:

- 📁 Dataset Upload
- 🧹 Data Cleaning
- 📊 Data Visualization
- 📈 Sales Analytics
- 🤖 AI Business Insights
- 🔮 Forecasting
- 📄 PDF Reports
""")

st.divider()

# -----------------------------
# Future Dashboard
# -----------------------------
left, right = st.columns(2)

with left:
    st.subheader("📈 Dashboard Preview")
    st.info("Sales charts will appear here after uploading a dataset.")

with right:
    st.subheader("🤖 AI Insights")
    st.info("Business insights will appear here after data analysis.")

st.divider()

st.success("🎉 Welcome! Upload a dataset to begin your analytics journey.")