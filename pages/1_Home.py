import streamlit as st

st.title("🏠 Home")

st.markdown("## Welcome to InsightIQ")

st.write(
    """
    InsightIQ is an AI-powered business analytics platform designed for
    retail and sales data.

    Upload your dataset to:
    - Analyze sales performance
    - Track KPIs
    - Generate business insights
    - Forecast future trends
    """
)

col1, col2, col3 = st.columns(3)

col1.metric("Analytics", "10+ Modules")
col2.metric("Charts", "20+ Visualizations")
col3.metric("Reports", "PDF & Excel")