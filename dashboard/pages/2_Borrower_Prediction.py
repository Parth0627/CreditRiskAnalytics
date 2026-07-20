import streamlit as st
import requests

st.set_page_config(page_title="Borrower Prediction", layout="wide")

st.title("👤 Borrower Risk Prediction")

st.write("Enter borrower details to estimate the Probability of Default.")

# -----------------------
# Input Form
# -----------------------

col1, col2 = st.columns(2)

with col1:
    loan_amnt = st.number_input("Loan Amount ($)", 1000, 40000, 10000)
    annual_inc = st.number_input("Annual Income ($)", 10000, 500000, 80000)
    int_rate = st.number_input("Interest Rate (%)", 5.0, 30.0, 11.5)
    dti = st.number_input("Debt-to-Income Ratio", 0.0, 60.0, 15.0)
    open_acc = st.number_input("Open Accounts", 0, 50, 8)

with col2:
    fico_low = st.number_input("FICO Low", 300, 850, 700)
    fico_high = st.number_input("FICO High", 300, 850, 704)
    revol_bal = st.number_input("Revolving Balance", 0, 500000, 12000)
    revol_util = st.number_input("Revolving Utilization (%)", 0.0, 150.0, 32.5)
    total_acc = st.number_input("Total Accounts", 1, 200, 18)

# -----------------------
# Predict Button
# -----------------------

if st.button("🔍 Predict Credit Risk", use_container_width=True):

    payload = {
        "data": {
            "loan_amnt": loan_amnt,
            "funded_amnt": loan_amnt,
            "funded_amnt_inv": loan_amnt,
            "annual_inc": annual_inc,
            "int_rate": int_rate,
            "dti": dti,
            "fico_range_low": fico_low,
            "fico_range_high": fico_high,
            "open_acc": open_acc,
            "revol_bal": revol_bal,
            "revol_util": revol_util,
            "total_acc": total_acc
        }
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=payload,
            timeout=10
        )

        result = response.json()

        st.success("Prediction Completed")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Probability of Default",
            f"{result['probability_of_default']*100:.2f}%"
        )

        c2.metric(
            "Risk Level",
            result["risk_level"]
        )

        c3.metric(
            "Recommendation",
            result["recommendation"]
        )

        if result["risk_level"] == "Low":
            st.success("🟢 Low Risk Borrower")

        elif result["risk_level"] == "Medium":
            st.warning("🟡 Medium Risk Borrower")

        else:
            st.error("🔴 High Risk Borrower")

    except Exception as e:

        st.error("Unable to connect to FastAPI server.")
        st.code(str(e))