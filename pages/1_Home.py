import streamlit as st
from utils.ui import load_custom_css

# --------------------------------------------------
# Load Theme
# --------------------------------------------------

load_custom_css()

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.markdown("""
<div class="hero-box">

<h1>🚀 InsightIQ</h1>

<h2>Enterprise Retail Intelligence Platform</h2>

<p>
Transform raw retail sales data into AI-powered business intelligence.
Analyze sales, generate dashboards, forecast future trends,
and receive intelligent recommendations in one platform.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# --------------------------------------------------
# QUICK ACTIONS
# --------------------------------------------------

st.subheader("🚀 Quick Actions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📤 Upload Dataset", use_container_width=True):
        st.switch_page("pages/2_Upload.py")

with col2:
    if st.button("📊 Dashboard", use_container_width=True):
        st.switch_page("pages/5_Dashboard.py")

with col3:
    if st.button("🤖 AI Insights", use_container_width=True):
        st.switch_page("pages/AI_Insights.py")

st.write("")
st.divider()

# --------------------------------------------------
# PLATFORM MODULES
# --------------------------------------------------

st.subheader("✨ Platform Modules")

row1 = st.columns(3)

with row1[0]:
    st.info(
        """
### 📤 Upload

Import CSV / Excel retail datasets.
"""
    )

with row1[1]:
    st.info(
        """
### 🧹 Cleaning

Handle missing values, duplicates and validation.
"""
    )

with row1[2]:
    st.info(
        """
### 📊 EDA

Visualize trends and explore business insights.
"""
    )

row2 = st.columns(3)

with row2[0]:
    st.info(
        """
### 📈 Dashboard

Interactive KPIs and charts.
"""
    )

with row2[1]:
    st.info(
        """
### 🤖 AI Insights

Generate intelligent business recommendations.
"""
    )

with row2[2]:
    st.info(
        """
### 🔮 Forecasting

Predict future sales using AI models.
"""
    )

st.divider()

st.subheader("📈 Analytics Workflow")

workflow = st.columns(6)

steps = [
    "📤 Upload",
    "🧹 Cleaning",
    "📊 EDA",
    "📈 Dashboard",
    "🤖 AI",
    "📄 Reports",
]

for col, step in zip(workflow, steps):
    with col:
        st.success(step)

st.divider()

st.subheader("🛠 Technology Stack")

t1, t2, t3, t4 = st.columns(4)

with t1:
    st.metric("Language", "Python")

with t2:
    st.metric("Framework", "Streamlit")

with t3:
    st.metric("AI Engine", "OpenRouter")

with t4:
    st.metric("Charts", "Plotly")

st.divider()
