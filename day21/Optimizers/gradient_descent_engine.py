import numpy as np


class GradientDescentEngine:
    def __init__(self, learning_rate: float = 0.05, epochs: int = 500):
        self.lr = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = 0.0
        self.loss_history: list[float] = []

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        m, n = X.shape
        self.weights = np.zeros(n)
        self.bias = 0.0

        for _ in range(self.epochs):
            # Forward pass: y_hat = Xw + b
            y_pred = np.dot(X, self.weights) + self.bias

            # Loss: MSE
            loss = (1.0 / (2.0 * m)) * np.sum((y_pred - y) ** 2)
            self.loss_history.append(float(loss))

            # Backward pass (gradients)
            dw = (1.0 / m) * np.dot(X.T, (y_pred - y))
            db = (1.0 / m) * np.sum(y_pred - y)

            # Gradient descent step
            self.weights -= self.lr * dw
            self.bias -= self.lr * db


if __name__ == "__main__":
    np.random.seed(42)
    X_synthetic = np.random.randn(100, 3)
    # Ground truth: y = 2.5*x0 - 1.5*x1 + 0.5*x2 + 4.0
    true_w = np.array([2.5, -1.5, 0.5])
    y_synthetic = np.dot(X_synthetic, true_w) + 4.0 + np.random.randn(100) * 0.05

    engine = GradientDescentEngine(learning_rate=0.1, epochs=300)
    engine.fit(X_synthetic, y_synthetic)

    print("=== Pure NumPy Gradient Descent Optimization ===")
    print(f"Initial Loss : {engine.loss_history[0]:.4f}")
    print(f"Final Loss   : {engine.loss_history[-1]:.6f}")
    print(f"Learned Weights: {np.round(engine.weights, 4)} (Expected: {true_w})")
    print(f"Learned Bias   : {engine.bias:.4f} (Expected: 4.0)")
    