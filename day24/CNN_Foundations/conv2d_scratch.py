import numpy as np


def conv2d(input_mat: np.ndarray, kernel: np.ndarray, stride: int = 1, padding: int = 0) -> np.ndarray:
    """Computes single-channel 2D spatial convolution without external deep learning libraries."""
    if padding > 0:
        input_padded = np.pad(input_mat, pad_width=padding, mode="constant", constant_values=0)
    else:
        input_padded = input_mat

    h_in, w_in = input_padded.shape
    k_h, k_w = kernel.shape

    out_h = (h_in - k_h) // stride + 1
    out_w = (w_in - k_w) // stride + 1
    output = np.zeros((out_h, out_w), dtype=np.float32)

    for i in range(out_h):
        for j in range(out_w):
            r_start = i * stride
            c_start = j * stride
            window = input_padded[r_start:r_start + k_h, c_start:c_start + k_w]
            output[i, j] = np.sum(window * kernel)

    return output


if __name__ == "__main__":
    # 5x5 Synthetic grayscale input patch
    input_feature = np.array([
        [1.0, 1.0, 1.0, 0.0, 0.0],
        [0.0, 1.0, 1.0, 1.0, 0.0],
        [0.0, 0.0, 1.0, 1.0, 1.0],
        [0.0, 0.0, 1.0, 1.0, 0.0],
        [0.0, 1.0, 1.0, 0.0, 0.0],
    ], dtype=np.float32)

    # 3x3 Vertical Sobel-like edge detector
    kernel_weights = np.array([
        [1.0, 0.0, -1.0],
        [1.0, 0.0, -1.0],
        [1.0, 0.0, -1.0],
    ], dtype=np.float32)

    out_map = conv2d(input_feature, kernel_weights, stride=1, padding=0)

    print("=== 2D Convolution Spatial Filter ===")
    print(f"Input Shape  : {input_feature.shape}")
    print(f"Kernel Shape : {kernel_weights.shape}")
    print(f"Output Shape : {out_map.shape} (Expected: (3, 3))")
    print("Output Feature Map:\n", out_map)