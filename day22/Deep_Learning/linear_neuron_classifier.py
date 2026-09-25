import numpy as np


class LinearNeuron:
    def __init__(self, lr: float = 0.1, epochs: int = 500):
        self.lr = lr
        self.epochs = epochs
        self.w = None
        self.b = 0.0

    @staticmethod
    def _sigmoid(z: np.ndarray) -> np.ndarray:
        return 1.0 / (1.0 + np.exp(-np.clip(z, -250, 250)))

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        m, n = X.shape
        self.w = np.zeros(n)
        self.b = 0.0

        for _ in range(self.epochs):
            # Forward pass: logit -> sigmoid activation
            z = np.dot(X, self.w) + self.b
            a = self._sigmoid(z)

            # Gradient calculation
            dw = (1.0 / m) * np.dot(X.T, (a - y))
            db = (1.0 / m) * np.sum(a - y)

            # Gradient descent update
            self.w -= self.lr * dw
            self.b -= self.lr * db

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        return self._sigmoid(np.dot(X, self.w) + self.b)

    def predict(self, X: np.ndarray) -> np.ndarray:
        return (self.predict_proba(X) >= 0.5).astype(int)


if __name__ == "__main__":
    np.random.seed(42)
    # Generate 2 linearly distinct clusters
    cluster1 = np.random.randn(50, 2) + np.array([2.0, 2.0])
    cluster2 = np.random.randn(50, 2) + np.array([-2.0, -2.0])
    X_data = np.vstack([cluster1, cluster2])
    y_data = np.array([1] * 50 + [0] * 50)

    neuron = LinearNeuron(lr=0.5, epochs=300)
    neuron.fit(X_data, y_data)
    acc = np.mean(neuron.predict(X_data) == y_data)

    print("=== Sigmoid Single-Layer Neuron Classifier ===")
    print(f"Weights : {neuron.w}")
    print(f"Bias    : {neuron.b:.4f}")
    print(f"Accuracy: {acc * 100:.2f}%")