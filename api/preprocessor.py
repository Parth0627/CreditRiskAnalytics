import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

FEATURE_COLUMNS = joblib.load(
    BASE_DIR / "models" / "feature_columns.pkl"
)


def preprocess_input(user_input: dict) -> pd.DataFrame:
    """
    Convert business inputs into the feature format expected by the model.
    Missing features are filled with 0.
    """

    df = pd.DataFrame([user_input])

    # Add any missing columns
    for col in FEATURE_COLUMNS:
        if col not in df.columns:
            df[col] = 0

    # Keep only training columns and in the correct order
    df = df[FEATURE_COLUMNS]

    return df