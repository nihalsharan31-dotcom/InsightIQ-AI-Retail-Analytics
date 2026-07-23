import streamlit as st
from utils.auth import require_dataset

require_dataset()
from utils.session_manager import (
    has_dataset,
    get_dataset,
)

from utils.ui import load_custom_css

from ai.ai_assistant import ask_business_ai

from ai.chat_memory import (
    initialize_chat,
    add_message,
    get_chat_history,
)

from ai.suggestions import (
    SUGGESTED_QUESTIONS,
)

# =====================================================
# LOAD CSS
# =====================================================

load_custom_css()

# =====================================================
# HERO
# =====================================================

st.markdown("""
<div class="hero-box">
<h1>🤖 AI Business Analyst</h1>
<h3>Your Intelligent Retail Assistant</h3>
<p>
Ask business questions, discover hidden insights,
analyze sales trends, and receive AI-powered
recommendations from your retail dataset.
</p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# DATASET CHECK
# =====================================================

if not has_dataset():
    st.warning("⚠️ Please upload a dataset first.")
    st.stop()

initialize_chat()

df = get_dataset()

st.success("✅ AI Assistant Ready")

st.write("")
st.divider()

# =====================================================
# SUGGESTED QUESTIONS
# =====================================================

st.markdown("""
<div class="glass-card">
<h3>💡 Suggested Business Questions</h3>
</div>
""", unsafe_allow_html=True)

cols = st.columns(2)

for i, question in enumerate(SUGGESTED_QUESTIONS):

    if cols[i % 2].button(question):

        with st.spinner("🤖 Thinking..."):

            answer = ask_business_ai(
                df,
                question
            )

        add_message("User", question)
        add_message("AI", answer)

st.write("")
st.divider()

# =====================================================
# CUSTOM QUESTION
# =====================================================

st.markdown("""
<div class="glass-card">
<h3>📝 Ask Your Own Question</h3>
</div>
""", unsafe_allow_html=True)

question = st.text_input(
    "Ask anything about your retail business..."
)

if st.button("🚀 Ask AI"):

    if question.strip():

        with st.spinner("Analyzing dataset..."):

            answer = ask_business_ai(
                df,
                question
            )

        add_message("User", question)
        add_message("AI", answer)

st.write("")
st.divider()

# =====================================================
# CHAT HISTORY
# =====================================================

st.markdown("""
<div class="glass-card">
<h3>💬 AI Conversation</h3>
</div>
""", unsafe_allow_html=True)

history = get_chat_history()

if not history:

    st.info("Start by asking a business question.")

else:

    for msg in history:

        if msg["role"] == "User":

            st.markdown(
                f"""
<div style="
background:#1E293B;
padding:15px;
border-radius:15px;
margin-bottom:10px;
border-left:5px solid #06B6D4;
">

<b>🧑 You</b><br><br>

{msg["content"]}

</div>
""",
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f"""
<div style="
background:#312E81;
padding:15px;
border-radius:15px;
margin-bottom:20px;
border-left:5px solid #8B5CF6;
">

<b>🤖 InsightIQ AI</b><br><br>

{msg["content"]}

</div>
""",
                unsafe_allow_html=True
            )