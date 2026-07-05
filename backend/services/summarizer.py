def generate_summary(analysis, cleaning):

    summary = []

    summary.append(
        f"The dataset contains {analysis['rows']} rows and {analysis['columns']} columns."
    )

    if cleaning["duplicates_removed"] == 0:
        summary.append("No duplicate rows were found.")
    else:
        summary.append(
            f"{cleaning['duplicates_removed']} duplicate rows were removed."
        )

    total_missing = sum(analysis["missing_values"].values())

    if total_missing == 0:
        summary.append("No missing values were detected.")
    else:
        summary.append(
            f"The dataset contains {total_missing} missing values."
        )

    summary.append("The dataset is ready for visualization.")

    return summary