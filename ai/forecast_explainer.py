from ai.llm_client import ask_llm


def explain_forecast(forecast_summary: str) -> str:
    """
    Generate AI-powered business insights for the sales forecast.
    """

    prompt = f"""
You are a Senior Business Intelligence Analyst.

Analyze the sales forecast below and provide business insights.

Forecast Data:
{forecast_summary}

Return ONLY valid Markdown.

Format exactly like this:

## Summary

Write one short paragraph.

## Key Insights

- Insight 1
- Insight 2
- Insight 3

## Business Recommendations

- Recommendation 1
- Recommendation 2
- Recommendation 3

Do not use HTML.
Do not use tables.
Do not use LaTeX.
"""

    return ask_llm(prompt)