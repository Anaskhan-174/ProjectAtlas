import pandas as pd


def clean_dataframe(df):

    original_rows = len(df)

    # Remove duplicate rows
    df = df.drop_duplicates()

    duplicates_removed = original_rows - len(df)

    # Clean text columns
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].str.strip()

    # Standardize column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    return df, {
        "duplicates_removed": duplicates_removed,
        "final_rows": len(df)
    }