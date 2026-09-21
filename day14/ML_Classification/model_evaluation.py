import numpy as np
from sklearn.metrics import classification_report


def compute_confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray) -> tuple[int, int, int, int]:
    tp = int(np.sum((y_true == 1) & (y_pred == 1)))
    fp = int(np.sum((y_true == 0) & (y_pred == 1)))
    tn = int(np.sum((y_true == 0) & (y_pred == 0)))
    fn = int(np.sum((y_true == 1) & (y_pred == 0)))
    return tp, fp, tn, fn


def compute_metrics(tp: int, fp: int, tn: int, fn: int) -> dict[str, float]:
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = (
        2.0 * (precision * recall) / (precision + recall)
        if (precision + recall) > 0
        else 0.0
    )
    accuracy = (tp + tn) / (tp + fp + tn + fn)
    return {
        "Accuracy": round(accuracy, 4),
        "Precision": round(precision, 4),
        "Recall": round(recall, 4),
        "F1_Score": round(f1, 4),
    }


if __name__ == "__main__":
    np.random.seed(42)
    y_actual = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 0])
    y_predicted = np.array([1, 0, 1, 0, 0, 1, 1, 0, 1, 0])

    tp, fp, tn, fn = compute_confusion_matrix(y_actual, y_predicted)
    metrics = compute_metrics(tp, fp, tn, fn)

    print(f"Confusion Matrix -> TP: {tp}, FP: {fp}, TN: {tn}, FN: {fn}")
    for k, v in metrics.items():
        print(f"{k}: {v}")

    print("\n--- Scikit-Learn Verification ---")
    print(classification_report(y_actual, y_predicted, digits=4))