import streamlit as st


def load_custom_css():
    """Load global CSS styling."""

    st.markdown(
        """
        <style>

        /* ----------------------------
           Main Layout
        ---------------------------- */

        .main {
            padding: 1rem 2rem;
        }

        /* ----------------------------
           Headings
        ---------------------------- */

        h1{
            color:#1E3A8A;
            font-size:42px;
            font-weight:700;
        }

        h2{
            color:#334155;
            font-weight:600;
        }

        h3{
            color:#475569;
        }

        /* ----------------------------
           KPI Cards
        ---------------------------- */

        div[data-testid="stMetric"]{
            background:#ffffff;
            border:1px solid #E2E8F0;
            border-radius:16px;
            padding:18px;
            box-shadow:0px 4px 12px rgba(0,0,0,.08);
        }

        /* ----------------------------
           Buttons
        ---------------------------- */

        .stButton>button{
            width:100%;
            height:46px;
            border-radius:10px;
            font-weight:600;
        }

        /* ----------------------------
           Sidebar
        ---------------------------- */

        section[data-testid="stSidebar"]{
            border-right:1px solid #E2E8F0;
        }

        /* ----------------------------
           Tables
        ---------------------------- */

        .stDataFrame{
            border-radius:12px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


def page_title(title: str, subtitle: str = ""):
    """Display a consistent page title."""

    st.title(title)

    if subtitle:
        st.caption(subtitle)

    st.divider()


def section_header(title: str):
    """Display a consistent section header."""

    st.subheader(title)


def info_banner(message: str):
    """Display an informational banner."""

    st.info(message)