from fastapi import FastAPI
from api.schema import LoanApplication
from api.predictor import predict_risk

app = FastAPI(
    title="Credit Risk Analytics API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Credit Risk Analytics API is running."
    }


@app.post("/predict")
def predict(application: LoanApplication):
    return predict_risk(application.data)