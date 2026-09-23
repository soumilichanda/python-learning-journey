import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def build_pipeline() -> Pipeline:
    num_cols = ["tenure", "monthly_charges"]
    cat_cols = ["contract_type"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), num_cols),
            ("cat", OneHotEncoder(drop="first", sparse_output=False), cat_cols),
        ]
    )

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", LogisticRegression(random_state=42)),
        ]
    )
    return pipeline


if __name__ == "__main__":
    np.random.seed(42)
    n = 120
    df = pd.DataFrame({
        "tenure": np.random.randint(1, 72, size=n),
        "monthly_charges": np.random.uniform(20.0, 120.0, size=n),
        "contract_type": np.random.choice(["month-to-month", "one-year", "two-year"], size=n),
    })
    y = np.random.choice([0, 1], size=n, p=[0.7, 0.3])

    pipe = build_pipeline()
    cv = StratifiedKFold(n_splits=4, shuffle=True, random_state=42)
    scores = cross_val_score(pipe, df, y, cv=cv, scoring="f1")

    print("=== Scikit-Learn Reusable Pipeline Evaluation ===")
    print(f"Cross-Validation F1 Scores : {np.round(scores, 4)}")
    print(f"Mean CV F1 Score           : {np.mean(scores):.4f}")