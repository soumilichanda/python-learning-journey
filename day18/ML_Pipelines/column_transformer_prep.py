import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def build_preprocessor() -> ColumnTransformer:
    numeric_features = ["age", "fare"]
    categorical_features = ["class_tier", "embarked"]

    transformer = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numeric_features),
            ("cat", OneHotEncoder(sparse_output=False, drop="first"), categorical_features),
        ],
        remainder="drop",
    )
    return transformer


if __name__ == "__main__":
    # Synthetic tabular dataset
    df = pd.DataFrame({
        "age": [22.0, 38.0, 26.0, 35.0, 54.0],
        "fare": [7.25, 71.28, 7.92, 53.10, 51.86],
        "class_tier": ["third", "first", "third", "first", "second"],
        "embarked": ["S", "C", "S", "S", "Q"],
    })

    preprocessor = build_preprocessor()
    transformed_matrix = preprocessor.fit_transform(df)

    print("=== ColumnTransformer Feature Preprocessing ===")
    print(f"Original Shape    : {df.shape}")
    print(f"Transformed Shape : {transformed_matrix.shape}")
    print(f"Output Feature Matrix (first 2 rows):\n{np.round(transformed_matrix[:2], 3)}")