import numpy as np


class DataLoader:
    def __init__(self, X: np.ndarray, y: np.ndarray, batch_size: int = 32, shuffle: bool = True, seed: int = 42):
        self.X = X
        self.y = y
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.seed = seed
        self.num_samples = X.shape[0]
        self.num_batches = int(np.ceil(self.num_samples / self.batch_size))
        self.rng = np.random.default_rng(self.seed)

    def __iter__(self):
        indices = np.arange(self.num_samples)
        if self.shuffle:
            self.rng.shuffle(indices)

        for i in range(0, self.num_samples, self.batch_size):
            batch_idx = indices[i:i + self.batch_size]
            yield self.X[batch_idx], self.y[batch_idx]

    def __len__(self) -> int:
        return self.num_batches


if __name__ == "__main__":
    # Generate 100 synthetic feature vectors with binary labels
    X_synthetic = np.random.randn(100, 4)
    y_synthetic = np.random.randint(0, 2, size=100)

    loader = DataLoader(X_synthetic, y_synthetic, batch_size=32, shuffle=True)
    print("=== Custom Mini-Batch DataLoader Inspection ===")
    print(f"Total instances: {len(X_synthetic)} | Expected batches: {len(loader)}")

    for batch_num, (x_batch, y_batch) in enumerate(loader):
        print(f"  Batch {batch_num + 1}: X shape={x_batch.shape}, y shape={y_batch.shape}")