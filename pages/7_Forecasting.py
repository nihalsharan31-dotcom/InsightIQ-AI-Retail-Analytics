import streamlit as st
import plotly.graph_objects as go

from utils.forecast import build_forecast_summary
from ai.forecast_explainer import explain_forecast
from utils.session_manager import has_dataset, get_dataset
from utils.forecast import (
    prepare_sales_data,
    forecast_sales,
)

st.title("📈 Sales Forecasting")

if not has_dataset():
    st.warning("Please upload a dataset first.")
    st.stop()

df = get_dataset()

sales_data = prepare_sales_data(df)

forecast_days = st.selectbox(
    "Forecast Period",
    [30, 60, 90],
    index=0
)

forecast_df = forecast_sales(
    sales_data,
    forecast_days
)

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=sales_data["ds"],
        y=sales_data["y"],
        mode="lines",
        name="Historical Sales",
    )
)

fig.add_trace(
    go.Scatter(
        x=forecast_df["ds"],
        y=forecast_df["Forecast"],
        mode="lines",
        name="Forecast",
    )
)

fig.update_layout(
    title="Sales Forecast",
    xaxis_title="Date",
    yaxis_title="Sales",
    hovermode="x unified",
)

st.plotly_chart(fig, use_container_width=True)

with st.expander("View Forecast Data"):
    st.dataframe(forecast_df)
    st.divider()

st.subheader("🤖 AI Forecast Insights")

if st.button("Generate AI Forecast Analysis"):

    with st.spinner("Analyzing forecast..."):

        summary = build_forecast_summary(
            sales_data,
            forecast_df
        )

        ai_report = explain_forecast(summary)

    st.markdown(ai_report)