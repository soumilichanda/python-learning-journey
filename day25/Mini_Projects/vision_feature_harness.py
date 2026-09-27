import numpy as np


class VisionFeatureHarness:
    """Multi-layer vision pipeline extracting feature maps and activation statistics."""

    def __init__(self):
        self.layer_history: list[dict] = []

    @staticmethod
    def conv2d_channel(x: np.ndarray, kernel: np.ndarray, stride: int = 1, padding: int = 1) -> np.ndarray:
        if padding > 0:
            x_padded = np.pad(x, pad_width=padding, mode="constant", constant_values=0.0)
        else:
            x_padded = x

        h_in, w_in = x_padded.shape
        kh, kw = kernel.shape
        out_h = (h_in - kh) // stride + 1
        out_w = (w_in - kw) // stride + 1
        out = np.zeros((out_h, out_w), dtype=np.float32)

        for i in range(out_h):
            for j in range(out_w):
                window = x_padded[i * stride:i * stride + kh, j * stride:j * stride + kw]
                out[i, j] = np.sum(window * kernel)

        return out

    @staticmethod
    def max_pool2d(x: np.ndarray, size: int = 2, stride: int = 2) -> np.ndarray:
        h_in, w_in = x.shape
        out_h = (h_in - size) // stride + 1
        out_w = (w_in - size) // stride + 1
        out = np.zeros((out_h, out_w), dtype=np.float32)

        for i in range(out_h):
            for j in range(out_w):
                window = x[i * stride:i * stride + size, j * stride:j * stride + size]
                out[i, j] = np.max(window)

        return out

    def extract_features(self, image: np.ndarray) -> np.ndarray:
        self.layer_history.clear()

        # Edge Filter (Kernel 1)
        edge_kernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], dtype=np.float32)
        conv1 = self.conv2d_channel(image, edge_kernel, stride=1, padding=1)
        relu1 = np.maximum(0.0, conv1)
        pool1 = self.max_pool2d(relu1, size=2, stride=2)

        self.layer_history.append({
            "stage": "Conv1_Edge + ReLU + Pool",
            "shape": pool1.shape,
            "mean_activation": float(np.mean(pool1)),
            "max_activation": float(np.max(pool1))
        })

        return pool1


if __name__ == "__main__":
    np.random.seed(42)
    # 8x8 Grayscale image patch
    mock_image = np.random.uniform(0.0, 1.0, size=(8, 8)).astype(np.float32)

    harness = VisionFeatureHarness()
    final_features = harness.extract_features(mock_image)

    print("=== Milestone 4: Vision Feature Extraction Harness ===")
    print(f"Input Resolution: {mock_image.shape}")
    for record in harness.layer_history:
        print(f"Stage: {record['stage']}")
        print(f"  Shape: {record['shape']} | Mean: {record['mean_activation']:.4f} | Max: {record['max_activation']:.4f}")