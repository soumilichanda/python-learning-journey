import numpy as np


def min_max_scaler(
    X_train: np.ndarray, X_test: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    x_min = np.min(X_train, axis=0)
    x_max = np.max(X_train, axis=0)
    # Prevent divide-by-zero
    scale = np.where((x_max - x_min) == 0, 1.0, x_max - x_min)

    X_train_scaled = (X_train - x_min) / scale
    X_test_scaled = (X_test - x_min) / scale
    return X_train_scaled, X_test_scaled


def standard_scaler(
    X_train: np.ndarray, X_test: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    mean = np.mean(X_train, axis=0)
    std = np.std(X_train, axis=0)
    # Prevent divide-by-zero
    scale = np.where(std == 0, 1.0, std)

    X_train_scaled = (X_train - mean) / scale
    X_test_scaled = (X_test - mean) / scale
    return X_train_scaled, X_test_scaled


if __name__ == "__main__":
    np.random.seed(42)
    train_feats = np.random.normal(loc=50.0, scale=15.0, size=(100, 2))
    test_feats = np.random.normal(loc=48.0, scale=14.0, size=(20, 2))

    # Min-Max Scaling
    norm_train, norm_test = min_max_scaler(train_feats, test_feats)
    print("MinMax Scaled Train - Min:", norm_train.min(axis=0), "Max:", norm_train.max(axis=0))
    print("MinMax Scaled Test  - Min:", np.round(norm_test.min(axis=0), 3), "Max:", np.round(norm_test.max(axis=0), 3))

    # Z-score Scaling
    std_train, std_test = standard_scaler(train_feats, test_feats)
    print("Standardized Train  - Mean:", np.round(std_train.mean(axis=0), 3), "Std:", np.round(std_train.std(axis=0), 3))
    print("Standardized Test   - Mean:", np.round(std_test.mean(axis=0), 3), "Std:", np.round(std_test.std(axis=0), 3))