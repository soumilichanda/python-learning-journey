import numpy as np


def horizontal_flip(image: np.ndarray) -> np.ndarray:
    return image[:, ::-1, :]


def adjust_brightness(image: np.ndarray, factor: float) -> np.ndarray:
    return np.clip(image + factor, 0.0, 1.0)


def add_gaussian_noise(image: np.ndarray, mean: float = 0.0, std: float = 0.05) -> np.ndarray:
    noise = np.random.normal(mean, std, image.shape)
    return np.clip(image + noise, 0.0, 1.0)


if __name__ == "__main__":
    np.random.seed(42)
    base_img = np.random.rand(128, 128, 3).astype(np.float32)

    flipped = horizontal_flip(base_img)
    brightened = adjust_brightness(base_img, factor=0.15)
    noisy = add_gaussian_noise(base_img, std=0.04)

    print("Augmentation Checks:")
    print(f"Original Shape    : {base_img.shape}")
    print(f"Flipped Identity  : {np.array_equal(flipped[:, ::-1, :], base_img)}")
    print(f"Mean Delta Bright : {brightened.mean() - base_img.mean():.4f}")
    print(f"Noisy In-Bounds   : {0.0 <= noisy.min() and noisy.max() <= 1.0}")