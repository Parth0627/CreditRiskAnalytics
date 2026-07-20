import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Model Performance", layout="wide")

st.title("📈 Model Performance")

st.markdown("### Model Comparison")

results = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "XGBoost",
        "LightGBM"
    ],
    "Accuracy":[
        0.9014,
        0.8894,
        0.9175,
        0.9206,
        0.8951
    ],
    "ROC_AUC":[
        0.9567,
        0.9571,
        0.9588,
        0.9630,
        0.9628
    ],
    "Precision":[
        0.738,
        0.708,
        0.770,
        0.786,
        0.683
    ],
    "Recall":[
        0.900,
        0.916,
        0.758,
        0.779,
        0.922
    ],
    "F1 Score":[
        0.811,
        0.799,
        0.764,
        0.782,
        0.785
    ]
})

st.dataframe(results, use_container_width=True)

st.divider()

col1, col2 = st.columns(2)

with col1:

    fig = px.bar(
        results,
        x="Model",
        y="ROC_AUC",
        color="ROC_AUC",
        title="ROC-AUC Comparison"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    fig = px.bar(
        results,
        x="Model",
        y="Accuracy",
        color="Accuracy",
        title="Accuracy Comparison"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("🏆 Best Model")

st.success("""
**XGBoost** was selected as the final deployment model.

Reasons:

- Highest ROC-AUC
- Highest Accuracy
- Excellent Precision-Recall balance
- Production ready
""")

st.info("""
LightGBM also achieved excellent performance and had the lowest False Negatives,
making it a strong alternative for business deployment.
""")