import streamlit as st
from utils.auth import require_dataset

require_dataset()
from utils.session_manager import (
    has_dataset,
    get_dataset,
)

from utils.charts import (
    create_histogram,
    create_box_plot,
)

from utils.ui import load_custom_css

# =====================================================
# LOAD CUSTOM CSS
# =====================================================

load_custom_css()

# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
<div class="hero-box">
    <h1>📊 Exploratory Data Analysis</h1>
    <h3>Understand Your Dataset Before AI Analysis</h3>
    <p>
        Explore your dataset using descriptive statistics and
        interactive visualizations to discover patterns,
        distributions, and outliers.
    </p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# CHECK DATASET
# =====================================================

if not has_dataset():
    st.warning("⚠️ Please upload a dataset first.")
    st.stop()

df = get_dataset()

st.success("✅ Dataset loaded successfully!")

st.write("")
st.divider()

# =====================================================
# DATASET OVERVIEW
# =====================================================

st.markdown("""
<div class="glass-card">
<h3>📊 Dataset Overview</h3>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("📄 Rows", df.shape[0])

with c2:
    st.metric("📑 Columns", df.shape[1])

with c3:
    st.metric(
        "🔢 Numeric Columns",
        len(df.select_dtypes(include="number").columns)
    )

st.write("")
st.divider()

# =====================================================
# STATISTICAL SUMMARY
# =====================================================

st.markdown("""
<div class="glass-card">
<h3>📋 Statistical Summary</h3>
</div>
""", unsafe_allow_html=True)

st.dataframe(
    df.describe(),
    use_container_width=True,
    height=350,
)

st.write("")
st.divider()

# =====================================================
# VISUAL ANALYSIS
# =====================================================

numeric_columns = list(
    df.select_dtypes(include="number").columns
)

if not numeric_columns:
    st.info("No numeric columns available.")
    st.stop()

st.markdown("""
<div class="glass-card">
<h3>📈 Interactive Visualizations</h3>
</div>
""", unsafe_allow_html=True)

selected_column = st.selectbox(
    "Select Numeric Column",
    numeric_columns,
)

col1, col2 = st.columns(2)

with col1:

    st.subheader("📊 Histogram")

    st.plotly_chart(
        create_histogram(df, selected_column),
        use_container_width=True,
    )

with col2:

    st.subheader("📦 Box Plot")

    st.plotly_chart(
        create_box_plot(df, selected_column),
        use_container_width=True,
    )

st.write("")
st.divider()

# =====================================================
# DATA INSIGHTS
# =====================================================

st.markdown("""
<div class="glass-card">
<h3>💡 Quick Insights</h3>
</div>
""", unsafe_allow_html=True)

st.success(f"✔ Total Records : {df.shape[0]:,}")

st.success(f"✔ Total Features : {df.shape[1]}")

st.success(f"✔ Numeric Features : {len(numeric_columns)}")

st.success(f"✔ Missing Values : {int(df.isnull().sum().sum())}")

st.success("✔ Dataset is ready for Dashboard & AI Analysis.")