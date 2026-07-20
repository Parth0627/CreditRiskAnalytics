import joblib
from pathlib import Path

from api.preprocessor import preprocess_input

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL = joblib.load(
    BASE_DIR / "models" / "xgboost_credit_risk.pkl"
)


def predict_risk(user_input: dict):

    X = preprocess_input(user_input)

    probability = float(MODEL.predict_proba(X)[0][1])

    prediction = int(MODEL.predict(X)[0])

    if probability < 0.30:
        risk = "Low"
        recommendation = "Approve"

    elif probability < 0.60:
        risk = "Medium"
        recommendation = "Manual Review"

    else:
        risk = "High"
        recommendation = "Reject"

    return {
        "prediction": prediction,
        "probability_of_default": round(probability, 4),
        "risk_level": risk,
        "recommendation": recommendation
    }