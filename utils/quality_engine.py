import pandas as pd


def generate_quality_report(df: pd.DataFrame):
    """
    Generate dataset quality report.
    """

    rows = df.shape[0]
    columns = df.shape[1]

    missing_values = int(df.isnull().sum().sum())
    duplicate_rows = int(df.duplicated().sum())

    numeric_columns = len(df.select_dtypes(include="number").columns)
    categorical_columns = len(df.select_dtypes(include="object").columns)
    datetime_columns = len(df.select_dtypes(include="datetime").columns)

    score = 100

    if missing_values > 0:
        score -= 20

    if duplicate_rows > 0:
        score -= 10

    score = max(score, 0)

    recommendations = []

    if missing_values == 0:
        recommendations.append("✔ No missing values found.")
    else:
        recommendations.append(
            f"⚠ Fill or remove {missing_values} missing values."
        )

    if duplicate_rows == 0:
        recommendations.append("✔ No duplicate rows found.")
    else:
        recommendations.append(
            f"⚠ Remove {duplicate_rows} duplicate rows."
        )

    if score >= 90:
        status = "Ready for Analysis"
    elif score >= 70:
        status = "Needs Minor Cleaning"
    else:
        status = "Needs Major Cleaning"

    return {
        "rows": rows,
        "columns": columns,
        "missing": missing_values,
        "duplicates": duplicate_rows,
        "numeric": numeric_columns,
        "categorical": categorical_columns,
        "datetime": datetime_columns,
        "score": score,
        "status": status,
        "recommendations": recommendations,
    }