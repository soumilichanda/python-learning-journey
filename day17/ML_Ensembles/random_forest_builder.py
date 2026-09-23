import numpy as np
from sklearn.tree import DecisionTreeClassifier


class SimpleRandomForest:
    def __init__(self, n_estimators: int = 5, max_depth: int = 3, max_features: float = 0.8):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.max_features = max_features
        self.trees: list[DecisionTreeClassifier] = []
        self.feature_indices: list[np.ndarray] = []

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        n_samples, n_features = X.shape
        num_sub_features = int(np.ceil(self.max_features * n_features))

        for _ in range(self.n_estimators):
            # 1. Bootstrap sampling with replacement
            sample_idxs = np.random.choice(n_samples, size=n_samples, replace=True)
            X_boot, y_boot = X[sample_idxs], y[sample_idxs]

            # 2. Random feature subsampling without replacement
            feat_idxs = np.random.choice(n_features, size=num_sub_features, replace=False)
            self.feature_indices.append(feat_idxs)

            # 3. Train base tree on bootstrapped data and feature subset
            tree = DecisionTreeClassifier(max_depth=self.max_depth, random_state=42)
            tree.fit(X_boot[:, feat_idxs], y_boot)
            self.trees.append(tree)

    def predict(self, X: np.ndarray) -> np.ndarray:
        # Collect predictions from all base estimators
        tree_preds = []
        for tree, feat_idxs in zip(self.trees, self.feature_indices):
            tree_preds.append(tree.predict(X[:, feat_idxs]))

        # Majority vote across estimators (axis=0)
        tree_preds = np.array(tree_preds)
        majority_votes = [
            int(np.bincount(tree_preds[:, col]).argmax())
            for col in range(X.shape[0])
        ]
        return np.array(majority_votes)


if __name__ == "__main__":
    np.random.seed(42)
    # Synthetic classification data (60 samples, 4 features)
    X_train = np.random.randn(60, 4)
    y_train = (X_train[:, 0] + X_train[:, 1] > 0.0).astype(int)

    rf = SimpleRandomForest(n_estimators=7, max_depth=3, max_features=0.75)
    rf.fit(X_train, y_train)
    predictions = rf.predict(X_train)

    accuracy = np.mean(predictions == y_train)
    print("=== Custom Random Forest Ensemble Diagnostics ===")
    print(f"Estimators Fitted : {len(rf.trees)}")
    print(f"Training Accuracy : {accuracy * 100:.2f}%")