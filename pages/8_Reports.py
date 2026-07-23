import streamlit as st
from pathlib import Path
from utils.auth import require_dataset

require_dataset()
from utils.ui import load_custom_css

from utils.session_manager import (
    has_dataset,
    get_dataset,
)

from utils.dashboard_metrics import calculate_kpis
from ai.dashboard_context import build_dashboard_context
from ai.dashboard_explainer import explain_dashboard
from utils.report import generate_report

# =====================================================
# LOAD CUSTOM CSS
# =====================================================

load_custom_css()

# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
<div class="hero-box">
    <h1>📄 Executive Reports</h1>
    <h3>AI-Powered Business Reporting</h3>
    <p>
        Generate professional executive reports containing
        business KPIs, AI-generated insights, and performance
        analysis for decision making.
    </p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# DATASET CHECK
# =====================================================

if not has_dataset():
    st.warning("⚠️ Please upload a dataset first.")
    st.stop()

df = get_dataset()

kpis = calculate_kpis(df)

st.success("✅ Dataset Ready for Report Generation")

st.write("")
st.divider()

# =====================================================
# REPORT OVERVIEW
# =====================================================

st.markdown("""
<div class="glass-card">
<h3>📋 Report Contents</h3>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.checkbox(
        "📊 Business KPIs",
        value=True,
        disabled=True
    )

with col2:
    st.checkbox(
        "🤖 AI Executive Summary",
        value=True,
        disabled=True
    )

st.info(
    "The generated report contains business KPIs and an AI-generated executive summary in PDF format."
)

st.write("")
st.divider()

# =====================================================
# REPORT GENERATION
# =====================================================

st.markdown("""
<div class="glass-card">
<h3>📄 Generate Executive Report</h3>
</div>
""", unsafe_allow_html=True)

st.write(
    "Click the button below to generate a professional PDF report."
)

if st.button("🚀 Generate Executive Report"):

    with st.spinner("Generating AI Business Report..."):

        context = build_dashboard_context(df)

        ai_summary = explain_dashboard(context)

    output_dir = Path("reports")
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / "executive_report.pdf"

    generate_report(
        kpis=kpis,
        ai_summary=ai_summary,
        output_path=str(output_path),
    )

    st.success("✅ Executive Report Generated Successfully!")

    with open(output_path, "rb") as pdf_file:

        st.download_button(
            label="⬇ Download Executive Report",
            data=pdf_file,
            file_name="InsightIQ_Executive_Report.pdf",
            mime="application/pdf",
            use_container_width=True,
        )

st.write("")
st.divider()

# =====================================================
# REPORT FEATURES
# =====================================================

st.markdown("""
<div class="glass-card">
<h3>✨ Report Features</h3>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.success("📊 Business KPIs")

with c2:
    st.success("🤖 AI Executive Summary")

with c3:
    st.success("📄 Professional PDF Format")