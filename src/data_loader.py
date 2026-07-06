import pandas as pd

from src.config import INTERIM_DATA_PATH


def load_dataset():
    """
    Loads the cleaned dataset from the interim folder.
    """

    df = pd.read_parquet(INTERIM_DATA_PATH)

    return df