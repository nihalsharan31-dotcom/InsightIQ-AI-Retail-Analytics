import streamlit as st
from utils.dashboard_filters import apply_filters
from utils.session_manager import (
    get_dataset,
    has_dataset,
)
from utils.dashboard_charts import (
    sales_by_category,
    sales_by_region,
    top_products,
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

st.caption(f"📁 Active Dataset: {len(df):,} records loaded")

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
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        sales_by_category(df),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        sales_by_region(df),
        use_container_width=True
    )

st.plotly_chart(
    top_products(df),
    use_container_width=True
)