import streamlit as st

st.set_page_config(
    page_title="Credit Risk Analytics",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Credit Risk Analytics Dashboard")

st.markdown("""
Welcome to the **Credit Risk Analytics System**.

This application predicts the **Probability of Default (PD)** for loan applicants
using an XGBoost model trained on Lending Club loan data.

### Modules
- 📊 Portfolio Dashboard
- 👤 Borrower Prediction
- 📈 Model Performance
""")

st.info("Select a page from the sidebar.")