import numpy as np
import pandas as pd


def create_loan_income_ratio(df):
    """
    Loan Amount / Annual Income
    Represents the proportion of annual income being borrowed.
    """

    df["loan_income_ratio"] = np.where(
        df["annual_inc"] > 0,
        df["loan_amnt"] / df["annual_inc"],
        np.nan
    )

    return df


def create_installment_income_ratio(df):
    """
    Monthly Installment / Annual Income
    Represents repayment burden relative to income.
    """

    df["installment_income_ratio"] = np.where(
        df["annual_inc"] > 0,
        df["installment"] / df["annual_inc"],
        np.nan
    )

    return df


def create_average_fico(df):
    """
    Average FICO Score
    """

    df["fico_average"] = (
        df["fico_range_low"] +
        df["fico_range_high"]
    ) / 2

    return df


def feature_engineering_pipeline(df):
    """
    Executes all feature engineering steps.
    """

    df = create_loan_income_ratio(df)

    df = create_installment_income_ratio(df)

    df = create_average_fico(df)

    return df