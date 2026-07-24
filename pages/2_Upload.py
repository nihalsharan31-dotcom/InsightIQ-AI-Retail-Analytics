import streamlit as st

from config import SUPPORTED_FILE_TYPES
from utils.file_handler import load_dataset
from utils.validators import validate_file
from utils.profiler import profile_dataset
from utils.quality_engine import generate_quality_report
from utils.session_manager import set_dataset
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
    <h1>📤 Upload Dataset</h1>
    <h3>Start Your AI Retail Analytics Journey</h3>
    <p>
        Upload your CSV or Excel dataset to begin data cleaning,
        visualization, AI-powered analytics, forecasting,
        and executive report generation.
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

# =====================================================
# FILE UPLOAD
# =====================================================

st.markdown("""
<h3 style="margin-bottom:10px;">📤 Upload Your Dataset</h3>

<p style="color:#94A3B8;margin-bottom:12px;">

</p>

<p style="color:#FFFFFF;font-size:17px;font-weight:600;margin-bottom:8px;">
📂 Choose a CSV or Excel File to begin AI-powered analytics.
</p>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "",
    type=SUPPORTED_FILE_TYPES,
    label_visibility="collapsed",
    help="Supported formats: CSV, XLSX"
)
st.caption("📄 Maximum file size: 200 MB • Supported formats: CSV, XLSX")

# =====================================================
# PROCESS DATASET
# =====================================================

if uploaded_file:

    valid, message = validate_file(uploaded_file)

    if not valid:
        st.error(message)
        st.stop()

    try:

        dataframe = load_dataset(uploaded_file)
        set_dataset(dataframe)

        st.success("✅ Dataset uploaded successfully!")

        profile = profile_dataset(dataframe)

        st.write("")
        st.divider()

        # =====================================================
        # DATASET SUMMARY
        # =====================================================

        st.markdown("""
        <div class="glass-card">
        <h3>📊 Dataset Summary</h3>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("📄 Rows", profile["Rows"])

        with col2:
            st.metric("📑 Columns", profile["Columns"])

        with col3:
            st.metric("❗ Missing Values", profile["Missing Values"])

        col4, col5, col6 = st.columns(3)

        with col4:
            st.metric("📌 Duplicate Rows", profile["Duplicate Rows"])

        with col5:
            st.metric(
                "💾 Memory Usage",
                f'{profile["Memory (MB)"]} MB'
            )

        with col6:
            st.metric(
                "🔢 Numeric Columns",
                profile["Numeric Columns"]
            )

        st.write("")
        st.divider()

        # =====================================================
        # DATASET PREVIEW
        # =====================================================

        st.markdown("""
        <div class="glass-card">
        <h3>👀 Dataset Preview</h3>
        </div>
        """, unsafe_allow_html=True)

        st.dataframe(
            dataframe.head(20),
            use_container_width=True,
            height=450
        )

        st.write("")
        st.divider()

        # =====================================================
        # DATA QUALITY REPORT
        # =====================================================

        quality = generate_quality_report(dataframe)

        st.markdown("""
        <div class="glass-card">
        <h3>⭐ Data Quality Report</h3>
        </div>
        """, unsafe_allow_html=True)

        q1, q2 = st.columns(2)

        with q1:
            st.metric(
                "Quality Score",
                f"{quality['score']}/100"
            )

        with q2:
            st.metric(
                "Status",
                quality["status"]
            )

        st.write("### 💡 Recommendations")

        for recommendation in quality["recommendations"]:
            st.success(recommendation)

        st.write("")
        st.divider()

        # =====================================================
        # DATA TYPES
        # =====================================================

        st.markdown("""
        <div class="glass-card">
        <h3>📋 Column Data Types</h3>
        </div>
        """, unsafe_allow_html=True)

        st.dataframe(
            dataframe.dtypes.astype(str).rename("Data Type"),
            use_container_width=True
        )

    except Exception as e:

        st.error(f"❌ {str(e)}")

else:

    st.info("👆 Upload a CSV or Excel dataset to begin analysis.")