import numpy as np


def compute_entropy(y: np.ndarray) -> float:
    if len(y) == 0:
        return 0.0
    _, counts = np.unique(y, return_counts=True)
    probabilities = counts / len(y)
    return float(-np.sum(probabilities * np.log2(probabilities + 1e-9)))


def compute_information_gain(y_parent: np.ndarray, y_left: np.ndarray, y_right: np.ndarray) -> float:
    n = len(y_parent)
    if n == 0 or len(y_left) == 0 or len(y_right) == 0:
        return 0.0
    h_parent = compute_entropy(y_parent)
    weighted_children = (len(y_left) / n) * compute_entropy(y_left) + (len(y_right) / n) * compute_entropy(y_right)
    return h_parent - weighted_children


def find_best_split(X_col: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    sorted_unique = np.sort(np.unique(X_col))
    thresholds = (sorted_unique[:-1] + sorted_unique[1:]) / 2.0

    best_ig = -1.0
    best_thresh = thresholds[0] if len(thresholds) > 0 else X_col[0]

    for t in thresholds:
        left_mask = X_col <= t
        right_mask = ~left_mask
        ig = compute_information_gain(y, y[left_mask], y[right_mask])
        if ig > best_ig:
            best_ig = ig
            best_thresh = t

    return best_thresh, best_ig


if __name__ == "__main__":
    np.random.seed(42)
    feature = np.array([2.5, 1.0, 3.2, 5.8, 6.1, 7.4, 1.2, 8.0])
    labels = np.array([0, 0, 0, 1, 1, 1, 0, 1])

    threshold, gain = find_best_split(feature, labels)
    print(f"Optimal Split Threshold : {threshold:.2f}")
    print(f"Maximum Information Gain: {gain:.4f}")