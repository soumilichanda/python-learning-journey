import numpy as np


class DiagnosticReport:
    def __init__(self, y_true: np.ndarray, y_pred: np.ndarray):
        self.y_true = y_true
        self.y_pred = y_pred
        self.tp = int(np.sum((y_true == 1) & (y_pred == 1)))
        self.tn = int(np.sum((y_true == 0) & (y_pred == 0)))
        self.fp = int(np.sum((y_true == 0) & (y_pred == 1)))
        self.fn = int(np.sum((y_true == 1) & (y_pred == 0)))

    def summary(self) -> dict:
        total = len(self.y_true)
        accuracy = (self.tp + self.tn) / total if total > 0 else 0.0
        precision = self.tp / (self.tp + self.fp) if (self.tp + self.fp) > 0 else 0.0
        recall = self.tp / (self.tp + self.fn) if (self.tp + self.fn) > 0 else 0.0
        specificity = self.tn / (self.tn + self.fp) if (self.tn + self.fp) > 0 else 0.0
        fpr = self.fp / (self.fp + self.tn) if (self.fp + self.tn) > 0 else 0.0
        f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0

        return {
            "Accuracy": round(accuracy, 4),
            "Precision": round(precision, 4),
            "Recall": round(recall, 4),
            "Specificity": round(specificity, 4),
            "False Positive Rate": round(fpr, 4),
            "F1-Score": round(f1, 4),
        }

    def print_report(self):
        print("=== Diagnostic Classification Report ===")
        print(f"Counts: TP={self.tp}, FP={self.fp}, TN={self.tn}, FN={self.fn}")
        for metric, val in self.summary().items():
            print(f"{metric:<20}: {val}")


if __name__ == "__main__":
    y_true = np.array([1, 0, 1, 1, 0, 0, 1, 0, 1, 0])
    y_pred = np.array([1, 0, 1, 0, 0, 1, 1, 0, 1, 0])

    report = DiagnosticReport(y_true, y_pred)
    report.print_report()