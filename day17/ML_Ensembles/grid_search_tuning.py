import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, StratifiedKFold


def execute_hyperparameter_grid(X: np.ndarray, y: np.ndarray) -> dict:
    param_grid = {
        "n_estimators": [10, 30, 50],
        "max_depth": [2, 4, None],
        "min_samples_split": [2, 5],
        "criterion": ["gini", "entropy"],
    }

    base_rf = RandomForestClassifier(random_state=42)
    cv_strategy = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)

    grid_search = GridSearchCV(
        estimator=base_rf,
        param_grid=param_grid,
        scoring="f1",
        cv=cv_strategy,
        n_jobs=-1,
    )
    grid_search.fit(X, y)

    return {
        "best_params": grid_search.best_params_,
        "best_f1_score": round(float(grid_search.best_score_), 4),
        "total_combinations_tested": len(grid_search.cv_results_["params"]),
    }


if __name__ == "__main__":
    np.random.seed(42)
    X = np.random.randn(100, 5)
    y = (X[:, 0] * 1.5 - X[:, 1] * 0.8 + np.random.randn(100) * 0.2 > 0.0).astype(int)

    results = execute_hyperparameter_grid(X, y)
    print("=== Exhaustive Hyperparameter Grid Search ===")
    print(f"Combinations Evaluated : {results['total_combinations_tested']}")
    print(f"Optimal Parameters     : {results['best_params']}")
    print(f"Best Stratified CV F1  : {results['best_f1_score']}")