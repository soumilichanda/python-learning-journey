import numpy as np


def compute_metrics(y_true: np.ndarray, y_probs: np.ndarray, threshold: float) -> tuple[float, float, float]:
    y_pred = (y_probs >= threshold).astype(int)
    tp = np.sum((y_true == 1) & (y_pred == 1))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
    return precision, recall, f1


if __name__ == "__main__":
    np.random.seed(42)
    # Synthetic ground-truth and model output probabilities
    y_true = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0])
    y_probs = np.array([0.91, 0.35, 0.67, 0.78, 0.12, 0.45, 0.22, 0.55, 0.88, 0.41, 0.60, 0.15])

    thresholds = np.linspace(0.1, 0.9, 9)
    best_f1 = -1.0
    best_threshold = 0.5

    print(f"{'Threshold':<10}{'Precision':<12}{'Recall':<10}{'F1-Score':<10}")
    print("-" * 42)
    for t in thresholds:
        p, r, f1 = compute_metrics(y_true, y_probs, t)
        print(f"{t:<10.1f}{p:<12.4f}{r:<10.4f}{f1:<10.4f}")
        if f1 > best_f1:
            best_f1 = f1
            best_threshold = t

    print("-" * 42)
    print(f"Optimal Threshold: {best_threshold:.1f} (Max F1: {best_f1:.4f})")