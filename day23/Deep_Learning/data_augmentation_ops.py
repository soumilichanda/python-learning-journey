import numpy as np


def random_horizontal_flip(images: np.ndarray, prob: float = 0.5) -> np.ndarray:
    """Randomly flips a batch of images along width (axis 2) given shape (B, H, W, C)."""
    batch_size = images.shape[0]
    flipped = images.copy()
    mask = np.random.rand(batch_size) < prob
    flipped[mask] = flipped[mask, :, ::-1, :]
    return flipped


def standardize_batch(images: np.ndarray) -> np.ndarray:
    """Channel-wise standardization for neural network input normalization."""
    # Compute mean and standard deviation per channel across batch, height, width
    mean = np.mean(images, axis=(0, 1, 2), keepdims=True)
    std = np.std(images, axis=(0, 1, 2), keepdims=True) + 1e-8
    return (images - mean) / std


if __name__ == "__main__":
    np.random.seed(42)
    # Simulate a mini-batch: 4 images of size 28x28 with 3 color channels
    batch_images = np.random.uniform(0.0, 1.0, size=(4, 28, 28, 3))

    augmented_batch = random_horizontal_flip(batch_images, prob=0.5)
    normalized_batch = standardize_batch(augmented_batch)

    print("=== Vectorized Augmentation & Normalization Engine ===")
    print(f"Original Batch Shape  : {batch_images.shape}")
    print(f"Augmented Batch Shape : {augmented_batch.shape}")
    print(f"Normalized Mean       : {np.mean(normalized_batch):.6f} (Expected: ~0.0)")
    print(f"Normalized Std Dev    : {np.std(normalized_batch):.6f} (Expected: ~1.0)")