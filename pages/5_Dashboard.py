import streamlit as st

from utils.ui import (
    load_custom_css,
    page_title,
    section_header,
)

from utils.session_manager import (
    get_dataset,
    has_dataset,
)

from utils.dashboard_filters import apply_filters
from utils.dashboard_metrics import calculate_kpis

from utils.dashboard_charts import (
    sales_by_category,
    sales_by_region,
    top_products,
)

from ai.dashboard_context import build_dashboard_context
from ai.dashboard_explainer import explain_dashboard
from ai.chart_explainer import explain_chart


# ---------------------------------------------------
# Page Styling
# ---------------------------------------------------

load_custom_css()

page_title(
    "📊 Business Dashboard",
    "AI-Powered Retail Analytics Platform"
)

# ---------------------------------------------------
# Check Dataset
# ---------------------------------------------------

if not has_dataset():
    st.warning("Please upload a dataset first.")
    st.stop()

df = get_dataset()

# ---------------------------------------------------
# Dashboard Filters
# ---------------------------------------------------

section_header("🔍 Dashboard Filters")

st.caption(
    "Filter the dataset by Region, Category, and Segment."
)

col1, col2, col3 = st.columns(3)

with col1:
    region = st.selectbox(
        "Region",
        ["All"] + sorted(df["Region"].unique().tolist())
    )

with col2:
    category = st.selectbox(
        "Category",
        ["All"] + sorted(df["Category"].unique().tolist())
    )

with col3:
    segment = st.selectbox(
        "Segment",
        ["All"] + sorted(df["Segment"].unique().tolist())
    )

df = apply_filters(
    df,
    region,
    category,
    segment,
)

st.caption(f"📁 Active Dataset: **{len(df):,}** records loaded")

# ---------------------------------------------------
# KPI Section
# ---------------------------------------------------

st.markdown("<br>", unsafe_allow_html=True)

section_header("📈 Business KPIs")

kpis = calculate_kpis(df)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Total Sales",
        f"${kpis['sales']:,.2f}"
    )

with col2:
    st.metric(
        "💵 Total Profit",
        f"${kpis['profit']:,.2f}"
    )

with col3:
    st.metric(
        "📦 Total Orders",
        f"{kpis['orders']:,}"
    )

with col4:
    st.metric(
        "📈 Average Sales",
        f"${kpis['average_sales']:,.2f}"
    )

# ---------------------------------------------------
# Charts Section
# ---------------------------------------------------

st.divider()

section_header("📊 Sales Analytics")

col1, col2 = st.columns(2)

# -----------------------------
# Sales by Category
# -----------------------------

with col1:

    st.plotly_chart(
        sales_by_category(df),
        use_container_width=True
    )

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    if st.button("✨ Explain Sales by Category"):

        with st.spinner("Analyzing chart..."):

            explanation = explain_chart(
                "Sales by Category",
                category_sales.to_string()
            )

        st.markdown(explanation)

# -----------------------------
# Sales by Region
# -----------------------------

with col2:

    st.plotly_chart(
        sales_by_region(df),
        use_container_width=True
    )

# ---------------------------------------------------
# Top Products
# ---------------------------------------------------

st.divider()

section_header("🏆 Top Products")

st.plotly_chart(
    top_products(df),
    use_container_width=True
)

# ---------------------------------------------------
# AI Executive Summary
# ---------------------------------------------------

st.divider()

section_header("🤖 AI Executive Summary")

st.caption(
    "Generate an AI-powered business summary based on the current dashboard."
)

if st.button("🚀 Generate Executive Summary"):

    with st.spinner("Generating AI insights..."):

        context = build_dashboard_context(df)

        report = explain_dashboard(context)

    st.markdown(report)