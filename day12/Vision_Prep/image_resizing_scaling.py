import numpy as np


def resize_nearest_neighbor(image: np.ndarray, target_shape: tuple[int, int]) -> np.ndarray:
    orig_h, orig_w, _ = image.shape
    target_h, target_w = target_shape

    row_indices = (np.linspace(0, orig_h - 1, target_h)).astype(int)
    col_indices = (np.linspace(0, orig_w - 1, target_w)).astype(int)

    return image[row_indices[:, None], col_indices]


def normalize_pixels(image: np.ndarray) -> np.ndarray:
    return image.astype(np.float32) / 255.0


if __name__ == "__main__":
    np.random.seed(42)
    synthetic_image = np.random.randint(0, 256, size=(300, 400, 3), dtype=np.uint8)
    print(f"Original Image Shape: {synthetic_image.shape}, Dtype: {synthetic_image.dtype}")

    resized = resize_nearest_neighbor(synthetic_image, (128, 128))
    print(f"Resized Shape       : {resized.shape}")

    normalized = normalize_pixels(resized)
    print(f"Normalized Dtype    : {normalized.dtype}")
    print(f"Min: {normalized.min():.4f}, Max: {normalized.max():.4f}, Mean: {normalized.mean():.4f}")