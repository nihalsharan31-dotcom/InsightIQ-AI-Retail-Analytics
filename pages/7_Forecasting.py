import streamlit as st
import plotly.graph_objects as go
from utils.auth import require_dataset

require_dataset()
from utils.ui import load_custom_css

from utils.forecast import (
    build_forecast_summary,
    prepare_sales_data,
    forecast_sales,
)

from ai.forecast_explainer import explain_forecast

from utils.session_manager import (
    has_dataset,
    get_dataset,
)

# =====================================================
# LOAD CUSTOM CSS
# =====================================================

load_custom_css()

# =====================================================
# HERO SECTION
# =====================================================

st.markdown("""
<div class="hero-box">
    <h1>📈 Sales Forecasting</h1>
    <h3>Predict Future Business Performance</h3>
    <p>
        Forecast future sales using historical business data,
        visualize predicted trends, and generate AI-powered
        business recommendations.
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

sales_data = prepare_sales_data(df)

st.success("✅ Forecasting Model Ready")

st.write("")
st.divider()

# =====================================================
# FORECAST SETTINGS
# =====================================================

st.markdown("""
<div class="glass-card">
<h3>⚙ Forecast Configuration</h3>
</div>
""", unsafe_allow_html=True)

forecast_days = st.selectbox(
    "Forecast Period",
    [30, 60, 90],
    index=0
)

forecast_df = forecast_sales(
    sales_data,
    forecast_days
)

st.write("")
st.divider()

# =====================================================
# FORECAST CHART
# =====================================================

st.markdown("""
<div class="glass-card">
<h3>📈 Sales Forecast Visualization</h3>
</div>
""", unsafe_allow_html=True)

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=sales_data["ds"],
        y=sales_data["y"],
        mode="lines",
        name="Historical Sales",
        line=dict(width=3)
    )
)

fig.add_trace(
    go.Scatter(
        x=forecast_df["ds"],
        y=forecast_df["Forecast"],
        mode="lines",
        name="Forecast",
        line=dict(width=3)
    )
)

fig.update_layout(

    title="Sales Forecast",

    xaxis_title="Date",

    yaxis_title="Sales",

    hovermode="x unified",

    template="plotly_dark",

    height=550,

    legend=dict(
        orientation="h",
        y=1.05
    )

)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.write("")
st.divider()

# =====================================================
# FORECAST TABLE
# =====================================================

st.markdown("""
<div class="glass-card">
<h3>📋 Forecast Data</h3>
</div>
""", unsafe_allow_html=True)

with st.expander("View Forecast Dataset", expanded=False):

    st.dataframe(
        forecast_df,
        use_container_width=True,
        height=350
    )

st.write("")
st.divider()

# =====================================================
# AI FORECAST ANALYSIS
# =====================================================

st.markdown("""
<div class="glass-card">
<h3>🤖 AI Forecast Insights</h3>
</div>
""", unsafe_allow_html=True)

st.write(
    "Generate an AI-powered explanation of future sales trends and business recommendations."
)

if st.button("🚀 Generate AI Forecast Analysis"):

    with st.spinner("Analyzing future sales..."):

        summary = build_forecast_summary(
            sales_data,
            forecast_df
        )

        ai_report = explain_forecast(summary)

    st.success("Forecast analysis completed successfully!")

    st.markdown(ai_report)