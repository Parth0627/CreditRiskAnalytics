import numpy as np

IDENTIFIER_COLUMNS = [
    "id",
    "member_id",
    "url"
]

LEAKAGE_COLUMNS = [
    "next_pymnt_d",
    "hardship_type",
    "hardship_reason",
    "hardship_status",
    "deferral_term",
    "hardship_amount",
    "hardship_start_date",
    "hardship_end_date",
    "payment_plan_start_date",
    "hardship_length",
    "hardship_dpd",
    "hardship_loan_status",
    "hardship_payoff_balance_amount",
    "hardship_last_payment_amount",
    "orig_projected_additional_accrued_interest",
    "debt_settlement_flag_date",
    "settlement_status",
    "settlement_date",
    "settlement_amount",
    "settlement_percentage",
    "settlement_term"
]

JOINT_APPLICATION_COLUMNS = [
    "annual_inc_joint",
    "verification_status_joint",
    "dti_joint",
    "revol_bal_joint",
    "sec_app_fico_range_low",
    "sec_app_fico_range_high",
    "sec_app_earliest_cr_line",
    "sec_app_inq_last_6mths",
    "sec_app_mort_acc",
    "sec_app_open_acc",
    "sec_app_revol_util",
    "sec_app_open_act_il",
    "sec_app_num_rev_accts",
    "sec_app_chargeoff_within_12_mths",
    "sec_app_collections_12_mths_ex_med",
    "sec_app_mths_since_last_major_derog"
]

COLUMNS_TO_REMOVE = (
    IDENTIFIER_COLUMNS
    + LEAKAGE_COLUMNS
    + JOINT_APPLICATION_COLUMNS
)


def create_target(df):

    df = df[
        df["loan_status"].isin(
            ["Fully Paid", "Charged Off"]
        )
    ].copy()

    df["target"] = np.where(
        df["loan_status"] == "Charged Off",
        1,
        0
    )

    return df


def remove_columns(df):

    return df.drop(columns=COLUMNS_TO_REMOVE)


def handle_missing_values(df):

    df["emp_length"] = df["emp_length"].fillna(
        df["emp_length"].mode()[0]
    )

    df["emp_title"] = df["emp_title"].fillna(
        "Unknown"
    )

    median_columns = [
        "mths_since_recent_inq",
        "num_tl_120dpd_2m",
        "mo_sin_old_il_acct"
    ]

    for column in median_columns:

        df[column] = df[column].fillna(
            df[column].median()
        )

    return df


def preprocess_dataset(df):

    df = create_target(df)

    df = remove_columns(df)

    df = handle_missing_values(df)

    return df