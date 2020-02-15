import pandas as pd
from sklearn.model_selection import train_test_split
from typing import Text, Tuple

def split_dataset_in_train_test(df: pd.DataFrame, test_size: float, random_state: int = 42) \
        -> Tuple[pd.DataFrame, pd.DataFrame]:

    dataset = df.copy()
    train_dataset, test_dataset = train_test_split(dataset, test_size=test_size, random_state=random_state)
    return train_dataset, test_dataset