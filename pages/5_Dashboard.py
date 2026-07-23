import streamlit as st
from utils.auth import require_dataset

require_dataset()
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
# Dataset Check
# ---------------------------------------------------

if not has_dataset():
    st.warning("Please upload a dataset first.")
    st.stop()

df = get_dataset()

# ---------------------------------------------------
# Filters
# ---------------------------------------------------

st.markdown("## 🔍 Dashboard Filters")

c1, c2, c3 = st.columns(3)

with c1:
    region = st.selectbox(
        "Region",
        ["All"] + sorted(df["Region"].unique().tolist())
    )

with c2:
    category = st.selectbox(
        "Category",
        ["All"] + sorted(df["Category"].unique().tolist())
    )

with c3:
    segment = st.selectbox(
        "Segment",
        ["All"] + sorted(df["Segment"].unique().tolist())
    )

df = apply_filters(df, region, category, segment)

st.info(f"📁 **{len(df):,} records** currently selected.")

# ---------------------------------------------------
# KPIs
# ---------------------------------------------------

kpis = calculate_kpis(df)

st.markdown("## 📈 Business Overview")

k1, k2, k3, k4 = st.columns(4)

k1.metric(
    "💰 Total Sales",
    f"${kpis['sales']:,.2f}"
)

k2.metric(
    "💵 Total Profit",
    f"${kpis['profit']:,.2f}"
)

k3.metric(
    "📦 Orders",
    f"{kpis['orders']:,}"
)

k4.metric(
    "📊 Avg Sales",
    f"${kpis['average_sales']:,.2f}"
)

st.divider()

# ---------------------------------------------------
# Charts
# ---------------------------------------------------

st.markdown("## 📊 Sales Analytics")

left, right = st.columns(2)

with left:

    st.subheader("Sales by Category")

    st.plotly_chart(
        sales_by_category(df),
        use_container_width=True
    )

    category_sales = (
        df.groupby("Category")["Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    if st.button("✨ AI Explain Category Sales"):

        with st.spinner("Generating explanation..."):

            explanation = explain_chart(
                "Sales by Category",
                category_sales.to_string()
            )

        st.success(explanation)

with right:

    st.subheader("Sales by Region")

    st.plotly_chart(
        sales_by_region(df),
        use_container_width=True
    )

st.divider()

# ---------------------------------------------------
# Top Products
# ---------------------------------------------------

st.markdown("## 🏆 Top Performing Products")

st.plotly_chart(
    top_products(df),
    use_container_width=True
)

st.divider()

# ---------------------------------------------------
# AI Summary
# ---------------------------------------------------

st.markdown("## 🤖 AI Executive Summary")

st.write(
    "Generate a management-level summary of the current dashboard."
)

if st.button("🚀 Generate Executive Summary"):

    with st.spinner("Analyzing business performance..."):

        context = build_dashboard_context(df)

        report = explain_dashboard(context)

    st.success(report)