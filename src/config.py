from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "accepted_2007_to_2018Q4.csv"

INTERIM_DATA_PATH = PROJECT_ROOT / "data" / "interim" / "credit_risk_cleaned.parquet"

PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed" / "credit_risk_features.parquet"

MODEL_PATH = PROJECT_ROOT / "models"