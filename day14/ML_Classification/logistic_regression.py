import numpy as np


class LogisticRegressionScratch:
    def __init__(self, lr: float = 0.05, n_iters: int = 1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def _sigmoid(self, z: np.ndarray) -> np.ndarray:
        return 1.0 / (1.0 + np.exp(-np.clip(z, -250, 250)))

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0.0

        for _ in range(self.n_iters):
            linear_model = np.dot(X, self.weights) + self.bias
            y_pred = self._sigmoid(linear_model)

            # Compute gradients
            dw = (1.0 / n_samples) * np.dot(X.T, (y_pred - y))
            db = (1.0 / n_samples) * np.sum(y_pred - y)

            # Update weights
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        linear_model = np.dot(X, self.weights) + self.bias
        return self._sigmoid(linear_model)

    def predict(self, X: np.ndarray, threshold: float = 0.5) -> np.ndarray:
        return (self.predict_proba(X) >= threshold).astype(int)


if __name__ == "__main__":
    np.random.seed(42)
    # Synthetic linearly separable data
    X_train = np.random.randn(100, 2)
    y_train = (X_train[:, 0] + X_train[:, 1] > 0).astype(int)

    clf = LogisticRegressionScratch(lr=0.1, n_iters=1000)
    clf.fit(X_train, y_train)

    X_test = np.random.randn(20, 2)
    preds = clf.predict(X_test)
    probs = clf.predict_proba(X_test)

    print("Model Weights:", np.round(clf.weights, 4))
    print("Model Bias   :", np.round(clf.bias, 4))
    print("Test Preds   :", preds[:5])
    print("Test Probs   :", np.round(probs[:5], 4))