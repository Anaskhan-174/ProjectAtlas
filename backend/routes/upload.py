from fastapi import APIRouter, UploadFile, File
from services.analyzer import analyze_dataframe
from services.cleaner import clean_dataframe
import pandas as pd
import os

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    if file.filename.endswith(".csv"):
        df = pd.read_csv(file_path)

    elif file.filename.endswith(".xlsx"):
        df = pd.read_excel(file_path)

    else:
        return {
            "error": "Only CSV and Excel files are allowed."
        }

    # Analyze original data
    analysis_report = analyze_dataframe(df)

    # Clean data
    cleaned_df, cleaning_report = clean_dataframe(df)

    # Analyze cleaned data
    cleaned_analysis = analyze_dataframe(cleaned_df)

    return {
        "original_analysis": analysis_report,
        "cleaning_report": cleaning_report,
        "cleaned_analysis": cleaned_analysis
    }