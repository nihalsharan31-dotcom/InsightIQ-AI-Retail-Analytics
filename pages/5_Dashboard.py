import streamlit as st
from utils.dashboard_filters import apply_filters
from utils.session_manager import (
    get_dataset,
    has_dataset,
)

from utils.dashboard_metrics import calculate_kpis

st.title("📊 Business Dashboard")

if not has_dataset():
    st.warning("Please upload a dataset first.")
    st.stop()

df = get_dataset()
st.divider()

st.subheader("Dashboard Filters")

col1, col2, col3 = st.columns(3)

region = col1.selectbox(
    "Region",
    ["All"] + sorted(df["Region"].unique().tolist())
)

category = col2.selectbox(
    "Category",
    ["All"] + sorted(df["Category"].unique().tolist())
)

segment = col3.selectbox(
    "Segment",
    ["All"] + sorted(df["Segment"].unique().tolist())
)

df = apply_filters(
    df,
    region,
    category,
    segment,
)

st.success("Dataset loaded successfully!")

kpis = calculate_kpis(df)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "💰 Total Sales",
    f"${kpis['sales']:,.2f}"
)

col2.metric(
    "💵 Total Profit",
    f"${kpis['profit']:,.2f}"
)

col3.metric(
    "📦 Total Orders",
    f"{kpis['orders']:,}"
)

col4.metric(
    "📈 Average Sales",
    f"${kpis['average_sales']:,.2f}"
)