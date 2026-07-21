import streamlit as st

def set_dataset(df):
    st.session_state["dataset"] = df

def get_dataset():
    return st.session_state.get("dataset")

def has_dataset():
    return "dataset" in st.session_state

def clear_dataset():
    st.session_state.pop("dataset", None)