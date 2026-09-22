import numpy as np
from sklearn.svm import SVC


def analyze_svm_margin(C_val: float, X: np.ndarray, y: np.ndarray) -> dict:
    clf = SVC(kernel="linear", C=C_val)
    clf.fit(X, y)

    w = clf.coef_[0]
    w_norm = np.linalg.norm(w)
    margin_width = 2.0 / w_norm if w_norm > 0 else 0.0

    return {
        "C": C_val,
        "Weights": np.round(w, 4),
        "Bias": round(float(clf.intercept_[0]), 4),
        "Margin_Width": round(margin_width, 4),
        "Support_Vectors_Count": int(len(clf.support_)),
    }


if __name__ == "__main__":
    np.random.seed(42)
    # Generate non-linearly perfect synthetic clusters
    X_pos = np.random.randn(25, 2) + np.array([2.0, 2.0])
    X_neg = np.random.randn(25, 2) + np.array([-2.0, -2.0])
    X = np.vstack([X_pos, X_neg])
    y = np.array([1] * 25 + [0] * 25)

    print("=== SVM Regularization Comparison (Margin Width vs Penalty C) ===")
    for c in [0.01, 1.0, 100.0]:
        stats = analyze_svm_margin(c, X, y)
        print(f"C={stats['C']:<6} | Margin: {stats['Margin_Width']:<8} | SVs: {stats['Support_Vectors_Count']}")