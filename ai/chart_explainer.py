from ai.llm_client import ask_llm


def explain_chart(chart_name: str, chart_data: str) -> str:
    """
    Generate AI explanation for a specific chart.
    """

    prompt = f"""
You are a Senior Business Intelligence Analyst.

Analyze ONLY the chart below.

Chart Name:
{chart_name}

Chart Data:
{chart_data}

Return ONLY valid Markdown.

Format exactly like this:

## Summary

Write one short paragraph.

## Key Findings

- Finding 1
- Finding 2
- Finding 3

## Business Recommendation

- Recommendation 1
- Recommendation 2

Do not use HTML.
Do not use tables.
Do not use LaTeX.
Do not use special formatting.
"""

    return ask_llm(prompt)