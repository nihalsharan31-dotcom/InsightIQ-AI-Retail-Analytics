from ai.llm_client import ask_llm


def explain_dashboard(context: str) -> str:
    """
    Generate an executive dashboard summary.
    """

    prompt = f"""
You are an expert Business Intelligence Analyst.

Using ONLY the dashboard information below,
prepare an executive report.

Dashboard Information
---------------------

{context}

Return the answer using this format:

# Executive Summary

# Key Insights

# Recommendations

# Risks

Keep the response concise.
"""

    return ask_llm(prompt)