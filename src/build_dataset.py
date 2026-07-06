import pandas as pd

from preprocess import preprocess_dataset

print("=" * 60)
print("Credit Risk Dataset Builder")
print("=" * 60)

print("\nLoading raw dataset...")

df = pd.read_csv(
    "../data/raw/accepted_2007_to_2018Q4.csv",
    low_memory=False
)

print(f"Dataset Loaded : {df.shape}")

print("\nStarting preprocessing...")

risk_df = preprocess_dataset(df)

print(f"Processed Dataset : {risk_df.shape}")

print("\nSaving dataset...")

risk_df.to_parquet(
    "../data/interim/credit_risk_cleaned.parquet",
    index=False
)

print("\nDataset saved successfully!")

print("=" * 60)