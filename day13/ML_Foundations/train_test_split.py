import numpy as np


def train_test_split_scratch(
    X: np.ndarray, y: np.ndarray, test_size: float = 0.2, random_state: int | None = None
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    if random_state is not None:
        np.random.seed(random_state)

    n_samples = X.shape[0]
    indices = np.arange(n_samples)
    np.random.shuffle(indices)

    n_test = int(n_samples * test_size)
    test_indices = indices[:n_test]
    train_indices = indices[n_test:]

    return X[train_indices], X[test_indices], y[train_indices], y[test_indices]


if __name__ == "__main__":
    np.random.seed(42)
    X = np.random.randn(100, 4)
    y = np.random.randint(0, 2, size=100)

    X_train, X_test, y_train, y_test = train_test_split_scratch(
        X, y, test_size=0.2, random_state=42
    )

    print(f"X_train shape: {X_train.shape}, y_train shape: {y_train.shape}")
    print(f"X_test shape : {X_test.shape}, y_test shape : {y_test.shape}")