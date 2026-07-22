import streamlit as st

from utils.session_manager import (
    has_dataset,
    get_dataset,
)

from ai.ai_assistant import ask_business_ai

from ai.chat_memory import (
    initialize_chat,
    add_message,
    get_chat_history,
)

from ai.suggestions import (
    SUGGESTED_QUESTIONS,
)

st.title("🤖 AI Business Analyst")

if not has_dataset():
    st.warning("Upload a dataset first.")
    st.stop()

initialize_chat()

df = get_dataset()

st.subheader("💡 Suggested Questions")

cols = st.columns(2)

for i, question in enumerate(SUGGESTED_QUESTIONS):

    if cols[i % 2].button(question):

        answer = ask_business_ai(df, question)

        add_message("User", question)
        add_message("AI", answer)

st.divider()

question = st.text_input(
    "Ask your own business question"
)

if st.button("Ask AI"):

    if question.strip():

        answer = ask_business_ai(
            df,
            question,
        )

        add_message("User", question)
        add_message("AI", answer)

st.divider()

st.subheader("💬 Conversation")

for msg in get_chat_history():

    if msg["role"] == "User":

        st.markdown(
            f"**🧑 You:** {msg['content']}"
        )

    else:

        st.markdown(
            f"**🤖 InsightIQ:** {msg['content']}"
        )