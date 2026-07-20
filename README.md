# Credit Risk Analytics

This project was developed as a part of my Machine Learning internship. The objective of this project is to build an end-to-end Credit Risk Analytics system that can predict whether a borrower is likely to default on a loan.

The project starts from raw loan data, performs preprocessing and feature engineering, compares multiple machine learning models and finally deploys the best model using FastAPI and Streamlit.

---

## Project Objective

The main goal of this project is to help financial institutions estimate the Probability of Default (PD) of loan applicants using machine learning.

The project covers the complete machine learning pipeline from data preprocessing to deployment.

---

## Dataset

Dataset Used: Lending Club Loan Dataset (2007–2018)

Dataset Size:
- Around 1.34 Million loan records
- 169 features after preprocessing and feature engineering

Target Variable:

- 0 → Fully Paid
- 1 → Charged Off

---

## Models Implemented

I trained and compared the following models:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- LightGBM

After comparing all the models, XGBoost was selected as the final model because it achieved the best overall performance.

---

## Model Performance

| Model | Accuracy | ROC-AUC |
|-------|---------:|---------:|
| Logistic Regression | 90.14% | 0.9567 |
| Decision Tree | 88.94% | 0.9571 |
| Random Forest | 91.75% | 0.9588 |
| XGBoost | **92.06%** | **0.9630** |
| LightGBM | 89.51% | 0.9628 |

---

## Technologies Used

Programming Language

- Python

Libraries

- Pandas
- NumPy
- Scikit-learn
- XGBoost
- LightGBM
- Plotly
- FastAPI
- Streamlit
- Joblib

---

## Project Structure

```text
CreditRiskAnalytics/

├── api/
├── dashboard/
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── models/
├── notebooks/
├── reports/
├── src/
├── requirements.txt
└── README.md
```

---

## Workflow

```
Raw Dataset
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Model Selection
      ↓
FastAPI
      ↓
Streamlit Dashboard
```

---

## Dashboard

The dashboard has three sections.

### Portfolio Dashboard

Shows overall portfolio statistics like

- Total loans
- Average loan amount
- Interest rate distribution
- Grade wise loan distribution
- Loan purpose distribution

### Borrower Prediction

Allows the user to enter borrower information and predicts

- Probability of Default
- Risk Level
- Recommendation (Approve / Manual Review / Reject)

### Model Performance

Shows

- Model comparison
- Accuracy comparison
- ROC-AUC comparison
- Final selected model

---

## How to Run

Clone the repository

```bash
git clone <repository-url>
cd CreditRiskAnalytics
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn api.main:app --reload
```

Open Swagger API

```
http://127.0.0.1:8000/docs
```

Run the dashboard

```bash
streamlit run dashboard/Home.py
```

---

## Future Improvements

There are still few improvements that can be done in future like

- Better hyperparameter tuning
- MLflow integration
- Docker deployment
- Cloud deployment
- SHAP for model explainability

---

## Author

Parth Pandya

B.Tech Computer Science Engineering

MIT World Peace University