import numpy as np
import pandas as pd

if __name__ == "__main__":
    raw_data = {
        "Name": ["Alok", "Bristi", "Charulata", "Dinesh", "Era"],
        "Age": [25, np.nan, 30, np.nan, 22],
        "Score": [88.0, 92.0, np.nan, 79.0, 85.0],
        "City": ["Bankura", "Kolkata", np.nan, "Bally", "Dankuni"],
    }
    df = pd.DataFrame(raw_data)

    # 1. Null detection
    print("Missing value counts:\n", df.isna().sum())

    # 2. Dropping missing entries
    dropped_df = df.dropna()
    print("\nDropped rows with nulls:\n", dropped_df)

    # 3. Imputation (mean for numeric, ffill/mode for categorical)
    imputed_df = df.copy()
    imputed_df["Age"] = imputed_df["Age"].fillna(imputed_df["Age"].mean())
    imputed_df["Score"] = imputed_df["Score"].fillna(imputed_df["Score"].median())
    imputed_df["City"] = imputed_df["City"].ffill()

    print("\nImputed DataFrame:\n", imputed_df)