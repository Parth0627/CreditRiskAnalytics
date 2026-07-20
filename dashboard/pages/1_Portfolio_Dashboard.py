import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Portfolio Dashboard", layout="wide")

st.title("📊 Loan Portfolio Dashboard")

# Load processed dataset
df = pd.read_parquet("data/processed/credit_risk_feature_engineered.parquet")

# ---------- KPIs ----------

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Loans", f"{len(df):,}")

col2.metric(
    "Average Loan Amount",
    f"${df['loan_amnt'].mean():,.0f}"
)

col3.metric(
    "Average Interest Rate",
    f"{df['int_rate'].mean():.2f}%"
)

default_rate = df["target"].mean() * 100

col4.metric(
    "Default Rate",
    f"{default_rate:.2f}%"
)

st.divider()

# ---------- Charts ----------

left, right = st.columns(2)

with left:

    fig = px.histogram(
        df,
        x="loan_amnt",
        nbins=50,
        title="Loan Amount Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    fig = px.histogram(
        df,
        x="int_rate",
        nbins=40,
        title="Interest Rate Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

left, right = st.columns(2)

with left:

    grade = (
        df["grade"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    grade.columns = ["Grade", "Count"]

    fig = px.bar(
        grade,
        x="Grade",
        y="Count",
        title="Loans by Grade"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    purpose = (
        df["purpose"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    purpose.columns = ["Purpose", "Count"]

    fig = px.pie(
        purpose,
        names="Purpose",
        values="Count",
        title="Top Loan Purposes"
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Dataset Preview")

st.dataframe(df.head(20), use_container_width=True)