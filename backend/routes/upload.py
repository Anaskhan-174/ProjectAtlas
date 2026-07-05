from fastapi import APIRouter, UploadFile, File
from services.analyzer import analyze_dataframe
from services.cleaner import clean_dataframe
from services.visualizer import generate_bar_chart
from services.summarizer import generate_summary
from services.dashboard_service import generate_dashboard
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

    # visualize   data in bar chart
    dashboard = generate_dashboard(cleaned_df)

    # for summry like output
    summary = generate_summary(
        cleaned_analysis,
        cleaning_report
    )

    return {
        "dashboard": dashboard,
        "summary": summary,
        "original_analysis": analysis_report,
        "cleaning_report": cleaning_report,
        "cleaned_analysis": cleaned_analysis
    }