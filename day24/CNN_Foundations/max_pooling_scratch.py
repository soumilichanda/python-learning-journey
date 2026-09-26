import numpy as np


def max_pool2d(input_mat: np.ndarray, pool_size: int = 2, stride: int = 2) -> np.ndarray:
    """Computes 2D Max Pooling on a 2D activation matrix."""
    h_in, w_in = input_mat.shape
    out_h = (h_in - pool_size) // stride + 1
    out_w = (w_in - pool_size) // stride + 1
    output = np.zeros((out_h, out_w), dtype=np.float32)

    for i in range(out_h):
        for j in range(out_w):
            r_start = i * stride
            c_start = j * stride
            window = input_mat[r_start:r_start + pool_size, c_start:c_start + pool_size]
            output[i, j] = np.max(window)

    return output


if __name__ == "__main__":
    activation_map = np.array([
        [12.0, 20.0, 30.0, 0.0],
        [8.0, 12.0, 2.0, 0.0],
        [34.0, 70.0, 37.0, 4.0],
        [112.0, 100.0, 25.0, 12.0],
    ], dtype=np.float32)

    pooled_map = max_pool2d(activation_map, pool_size=2, stride=2)

    print("=== Max Pooling 2D Downsampler ===")
    print(f"Input Shape  : {activation_map.shape}")
    print(f"Pooled Shape : {pooled_map.shape} (Expected: (2, 2))")
    print("Downsampled Activations:\n", pooled_map)