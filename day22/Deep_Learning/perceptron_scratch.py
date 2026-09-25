import numpy as np


class Perceptron:
    def __init__(self, learning_rate: float = 0.1, n_iterations: int = 50):
        self.lr = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = 0.0

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0.0

        for _ in range(self.n_iterations):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = 1 if linear_output >= 0.0 else 0

                # Perceptron learning rule
                update = self.lr * (y[idx] - y_predicted)
                self.weights += update * x_i
                self.bias += update

    def predict(self, X: np.ndarray) -> np.ndarray:
        linear_output = np.dot(X, self.weights) + self.bias
        return np.where(linear_output >= 0.0, 1, 0)


if __name__ == "__main__":
    # Linearly separable logic gate: OR
    X_or = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y_or = np.array([0, 1, 1, 1])

    clf = Perceptron(learning_rate=0.1, n_iterations=20)
    clf.fit(X_or, y_or)
    preds = clf.predict(X_or)

    print("=== Rosenblatt Perceptron (OR Gate) ===")
    print(f"Learned Weights: {clf.weights}")
    print(f"Learned Bias   : {clf.bias:.4f}")
    print(f"Predictions    : {preds.tolist()} (Expected: [0, 1, 1, 1])")