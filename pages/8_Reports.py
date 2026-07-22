import streamlit as st
from pathlib import Path

from utils.session_manager import (
    has_dataset,
    get_dataset,
)

from utils.dashboard_metrics import calculate_kpis
from ai.dashboard_context import build_dashboard_context
from ai.dashboard_explainer import explain_dashboard
from utils.report import generate_report


st.title("📄 Executive Reports")

st.write(
    """
Generate a professional AI-powered business report
based on your uploaded dataset.
"""
)

if not has_dataset():
    st.warning("Please upload a dataset first.")
    st.stop()

df = get_dataset()

kpis = calculate_kpis(df)

st.subheader("Report Contents")

st.checkbox("Business KPIs", value=True, disabled=True)
st.checkbox("AI Executive Summary", value=True, disabled=True)

st.divider()

if st.button("📄 Generate Executive Report"):

    with st.spinner("Generating AI Summary..."):

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

    st.success("✅ Report generated successfully!")

    with open(output_path, "rb") as pdf_file:
        st.download_button(
            label="⬇ Download Executive Report",
            data=pdf_file,
            file_name="InsightIQ_Executive_Report.pdf",
            mime="application/pdf",
        )