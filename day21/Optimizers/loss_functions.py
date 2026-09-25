import numpy as np


def mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> tuple[float, np.ndarray]:
    """Computes MSE loss and its analytical gradient with respect to predictions."""
    m = y_true.shape[0]
    loss = (1.0 / (2.0 * m)) * np.sum((y_pred - y_true) ** 2)
    grad = (1.0 / m) * (y_pred - y_true)
    return float(loss), grad


def softmax(z: np.ndarray) -> np.ndarray:
    """Softmax with max subtraction for numerical overflow prevention."""
    exp_shifted = np.exp(z - np.max(z, axis=1, keepdims=True))
    return exp_shifted / np.sum(exp_shifted, axis=1, keepdims=True)


def categorical_cross_entropy(y_true_one_hot: np.ndarray, logits: np.ndarray) -> tuple[float, np.ndarray]:
    """Computes CCE loss and gradient from raw unnormalized logits."""
    m = y_true_one_hot.shape[0]
    probs = softmax(logits)
    eps = 1e-15
    clipped_probs = np.clip(probs, eps, 1.0 - eps)

    loss = -(1.0 / m) * np.sum(y_true_one_hot * np.log(clipped_probs))
    # Combined analytical gradient: d(Loss)/d(logits)
    grad = (1.0 / m) * (probs - y_true_one_hot)
    return float(loss), grad


if __name__ == "__main__":
    y_t = np.array([[1.0], [2.0], [3.0]])
    y_p = np.array([[1.1], [1.9], [3.2]])
    mse_val, mse_grad = mean_squared_error(y_t, y_p)
    print(f"MSE Loss: {mse_val:.6f}")
    print(f"MSE Gradient:\n{mse_grad}")

    y_one_hot = np.array([[1, 0, 0], [0, 1, 0]])
    sample_logits = np.array([[2.0, 1.0, 0.1], [0.5, 2.5, 0.2]])
    cce_val, cce_grad = categorical_cross_entropy(y_one_hot, sample_logits)
    print(f"\nCCE Loss: {cce_val:.6f}")
    print(f"CCE Logit Gradient:\n{cce_grad}")