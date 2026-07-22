from ai.context_builder import build_context
from ai.prompts import SYSTEM_PROMPT
from ai.llm_client import ask_llm


def ask_business_ai(df, question: str) -> str:
    """
    Generate a business-aware AI response.
    """

    context = build_context(df)

    prompt = f"""
{SYSTEM_PROMPT}

Dataset Context
----------------
{context}

User Question
-------------
{question}

Instructions:
- Answer only from the dataset context.
- If information is unavailable, say so.
- Be concise.
- Give business recommendations where appropriate.
"""

    return ask_llm(prompt)