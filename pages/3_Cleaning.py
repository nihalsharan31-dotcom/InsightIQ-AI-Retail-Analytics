import streamlit as st
from utils.auth import require_dataset

require_dataset()
from utils.cleaner import (
    remove_duplicates,
    drop_missing,
    fill_missing_mean,
    fill_missing_median,
    fill_missing_mode,
)

from utils.session_manager import (
    get_dataset,
    has_dataset,
    set_dataset,
)

from utils.ui import load_custom_css

# =====================================================
# LOAD THEME
# =====================================================

load_custom_css()

# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
<div class="hero-box">
    <h1>🧹 Data Cleaning</h1>
    <h3>Prepare Your Dataset for AI Analytics</h3>
    <p>
        Clean and preprocess your dataset by removing duplicates,
        handling missing values, and improving data quality before
        visualization, AI insights, and forecasting.
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

st.success("✅ Dataset Loaded Successfully")

st.write("")
st.divider()

# =====================================================
# DATASET OVERVIEW
# =====================================================

st.markdown("""
<div class="glass-card">
<h3>📊 Current Dataset Overview</h3>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("📄 Rows", len(df))

with c2:
    st.metric("📑 Columns", len(df.columns))

with c3:
    st.metric("❗ Missing Values", int(df.isnull().sum().sum()))

st.write("")
st.divider()

# =====================================================
# CLEANING OPTIONS
# =====================================================

st.markdown("""
<div class="glass-card">
<h3>🧹 Cleaning Operations</h3>
</div>
""", unsafe_allow_html=True)

cleaning_option = st.selectbox(
    "Select Cleaning Method",
    [
        "Remove Duplicate Rows",
        "Drop Missing Rows",
        "Fill Missing (Mean)",
        "Fill Missing (Median)",
        "Fill Missing (Mode)"
    ]
)

if st.button("🚀 Clean Dataset"):

    if cleaning_option == "Remove Duplicate Rows":
        cleaned_df = remove_duplicates(df)

    elif cleaning_option == "Drop Missing Rows":
        cleaned_df = drop_missing(df)

    elif cleaning_option == "Fill Missing (Mean)":
        cleaned_df = fill_missing_mean(df)

    elif cleaning_option == "Fill Missing (Median)":
        cleaned_df = fill_missing_median(df)

    else:
        cleaned_df = fill_missing_mode(df)

    set_dataset(cleaned_df)

    st.success("✅ Dataset cleaned successfully!")

    st.write("")
    st.divider()

    # =====================================================
    # CLEANED PREVIEW
    # =====================================================

    st.markdown("""
    <div class="glass-card">
    <h3>👀 Cleaned Dataset Preview</h3>
    </div>
    """, unsafe_allow_html=True)

    st.dataframe(
        cleaned_df.head(20),
        use_container_width=True,
        height=450
    )

    st.write("")
    st.divider()

    # =====================================================
    # DOWNLOAD
    # =====================================================

    st.markdown("""
    <div class="glass-card">
    <h3>📥 Download Cleaned Dataset</h3>
    </div>
    """, unsafe_allow_html=True)

    csv = cleaned_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download Cleaned Dataset",
        data=csv,
        file_name="cleaned_dataset.csv",
        mime="text/csv",
        use_container_width=True,
    )