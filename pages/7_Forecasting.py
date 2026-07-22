import streamlit as st

from utils.session_manager import has_dataset, get_dataset
from utils.forecast import prepare_sales_data

st.title("📈 Sales Forecasting")

if not has_dataset():
    st.warning("Please upload a dataset first.")
    st.stop()

df = get_dataset()

sales_data = prepare_sales_data(df)

st.subheader("Prepared Time Series")

st.dataframe(sales_data)

st.success(f"Prepared {len(sales_data)} daily records for forecasting.")