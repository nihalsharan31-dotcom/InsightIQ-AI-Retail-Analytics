from datetime import datetime
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)


def generate_report(kpis, ai_summary, output_path):
    """
    Generate an executive PDF report.
    """

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(output_path)

    elements = []

    # -----------------------
    # Title
    # -----------------------

    elements.append(
        Paragraph(
            "<b><font size=20>InsightIQ</font></b>",
            styles["Title"],
        )
    )

    elements.append(
        Paragraph(
            "AI-Powered Retail Analytics Platform",
            styles["Heading2"],
        )
    )

    elements.append(Spacer(1, 20))

    # -----------------------
    # KPI Section
    # -----------------------

    elements.append(
        Paragraph(
            "<b>Business KPIs</b>",
            styles["Heading1"],
        )
    )

    elements.append(
        Paragraph(
            f"Total Sales : ${kpis['sales']:,.2f}",
            styles["BodyText"],
        )
    )

    elements.append(
        Paragraph(
            f"Total Profit : ${kpis['profit']:,.2f}",
            styles["BodyText"],
        )
    )

    elements.append(
        Paragraph(
            f"Total Orders : {kpis['orders']:,}",
            styles["BodyText"],
        )
    )

    elements.append(
        Paragraph(
            f"Average Sales : ${kpis['average_sales']:,.2f}",
            styles["BodyText"],
        )
    )

    elements.append(Spacer(1, 20))

    # -----------------------
    # AI Summary
    # -----------------------

    elements.append(
        Paragraph(
            "<b>AI Executive Summary</b>",
            styles["Heading1"],
        )
    )

    elements.append(
        Paragraph(
            ai_summary.replace("\n", "<br/>"),
            styles["BodyText"],
        )
    )

    elements.append(Spacer(1, 20))

    # -----------------------
    # Footer
    # -----------------------

    elements.append(
        Paragraph(
            f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M')}",
            styles["Italic"],
        )
    )

    doc.build(elements)