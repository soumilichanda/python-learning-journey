import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


class MLPipelineEngine:
    def __init__(self, numeric_cols: list[str], categorical_cols: list[str], random_state: int = 42):
        self.numeric_cols = numeric_cols
        self.categorical_cols = categorical_cols
        self.random_state = random_state
        self.models: dict[str, Pipeline] = {}
        self.preprocessor = self._build_preprocessor()

    def _build_preprocessor(self) -> ColumnTransformer:
        return ColumnTransformer(
            transformers=[
                ("num", StandardScaler(), self.numeric_cols),
                ("cat", OneHotEncoder(drop="first", sparse_output=False, handle_unknown="ignore"), self.categorical_cols),
            ],
            remainder="drop",
        )

    def train_test_split_scratch(
        self, df: pd.DataFrame, target_col: str, test_size: float = 0.2
    ) -> tuple[pd.DataFrame, pd.DataFrame, np.ndarray, np.ndarray]:
        np.random.seed(self.random_state)
        n = len(df)
        shuffled_indices = np.random.permutation(n)
        test_count = int(n * test_size)

        test_idx = shuffled_indices[:test_count]
        train_idx = shuffled_indices[test_count:]

        X = df.drop(columns=[target_col])
        y = df[target_col].to_numpy()

        return X.iloc[train_idx], X.iloc[test_idx], y[train_idx], y[test_idx]

    def fit_and_compare(self, X_train: pd.DataFrame, y_train: np.ndarray) -> None:
        model_candidates = {
            "Logistic_Regression": LogisticRegression(random_state=self.random_state),
            "Random_Forest": RandomForestClassifier(n_estimators=50, max_depth=5, random_state=self.random_state),
        }

        for name, estimator in model_candidates.items():
            pipe = Pipeline(steps=[("preprocessor", self.preprocessor), ("classifier", estimator)])
            pipe.fit(X_train, y_train)
            self.models[name] = pipe

    def evaluate_model(
        self, model_name: str, X_test: pd.DataFrame, y_test: np.ndarray, threshold: float = 0.5
    ) -> dict[str, float]:
        if model_name not in self.models:
            raise ValueError(f"Model '{model_name}' has not been trained yet.")

        pipeline = self.models[model_name]
        y_probs = pipeline.predict_proba(X_test)[:, 1]
        y_pred = (y_probs >= threshold).astype(int)

        tp = int(np.sum((y_test == 1) & (y_pred == 1)))
        fp = int(np.sum((y_test == 0) & (y_pred == 1)))
        tn = int(np.sum((y_test == 0) & (y_pred == 0)))
        fn = int(np.sum((y_test == 1) & (y_pred == 0)))

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
        accuracy = (tp + tn) / len(y_test) if len(y_test) > 0 else 0.0

        return {
            "Accuracy": round(accuracy, 4),
            "Precision": round(precision, 4),
            "Recall": round(recall, 4),
            "F1_Score": round(f1, 4),
            "TP": tp,
            "FP": fp,
            "TN": tn,
            "FN": fn,
        }

    def sweep_thresholds(
        self, model_name: str, X_test: pd.DataFrame, y_test: np.ndarray
    ) -> tuple[float, float]:
        pipeline = self.models[model_name]
        y_probs = pipeline.predict_proba(X_test)[:, 1]

        best_thresh = 0.5
        best_f1 = -1.0

        for thresh in np.linspace(0.1, 0.9, 9):
            metrics = self.evaluate_model(model_name, X_test, y_test, threshold=thresh)
            if metrics["F1_Score"] > best_f1:
                best_f1 = metrics["F1_Score"]
                best_thresh = float(thresh)

        return best_thresh, best_f1


if __name__ == "__main__":
    np.random.seed(42)
    sample_size = 200

    synthetic_df = pd.DataFrame({
        "age": np.random.randint(18, 70, size=sample_size),
        "income": np.random.uniform(25000, 120000, size=sample_size),
        "department": np.random.choice(["Sales", "Engineering", "Operations"], size=sample_size),
        "contract": np.random.choice(["Full-Time", "Contract"], size=sample_size),
        "churn": np.random.choice([0, 1], size=sample_size, p=[0.75, 0.25]),
    })

    engine = MLPipelineEngine(
        numeric_cols=["age", "income"],
        categorical_cols=["department", "contract"],
        random_state=42,
    )

    X_tr, X_te, y_tr, y_te = engine.train_test_split_scratch(synthetic_df, target_col="churn", test_size=0.25)
    engine.fit_and_compare(X_tr, y_tr)

    print("=== Milestone 2: ML Pipeline Engine Diagnostics ===")
    for model in ["Logistic_Regression", "Random_Forest"]:
        base_metrics = engine.evaluate_model(model, X_te, y_te, threshold=0.5)
        optimal_t, max_f1 = engine.sweep_thresholds(model, X_te, y_te)
        print(f"\n[{model}] Evaluation @ Default Threshold 0.5:")
        print(f"  Accuracy : {base_metrics['Accuracy']} | F1-Score : {base_metrics['F1_Score']}")
        print(f"  Confusion: TP={base_metrics['TP']}, FP={base_metrics['FP']}, TN={base_metrics['TN']}, FN={base_metrics['FN']}")
        print(f"  Optimal Threshold: {optimal_t:.2f} -> Max F1: {max_f1:.4f}")