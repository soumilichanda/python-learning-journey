import numpy as np


class ConvLayerActivationLogger:
    def __init__(self, in_channels: int, out_channels: int, kernel_size: int = 3):
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        # Shape: (out_channels, in_channels, kernel_size, kernel_size)
        self.kernels = np.random.randn(out_channels, in_channels, kernel_size, kernel_size) * 0.1

    def forward(self, x: np.ndarray) -> np.ndarray:
        # Input shape: (in_channels, H, W)
        c, h, w = x.shape
        kh = kw = self.kernel_size
        out_h, out_w = h - kh + 1, w - kw + 1
        out = np.zeros((self.out_channels, out_h, out_w), dtype=np.float32)

        for f in range(self.out_channels):
            for i in range(out_h):
                for j in range(out_w):
                    window = x[:, i:i + kh, j:j + kw]
                    out[f, i, j] = np.sum(window * self.kernels[f])

        # Apply ReLU activation
        return np.maximum(0.0, out)


if __name__ == "__main__":
    np.random.seed(42)
    # Simulated 3-channel (RGB) input patch: 3 x 8 x 8
    image_tensor = np.random.uniform(0.0, 1.0, size=(3, 8, 8)).astype(np.float32)

    layer = ConvLayerActivationLogger(in_channels=3, out_channels=4, kernel_size=3)
    activation_map = layer.forward(image_tensor)

    sparsity = np.mean(activation_map == 0.0)
    print("=== Multi-Channel Conv Activation Map Logger ===")
    print(f"Input Shape          : {image_tensor.shape}")
    print(f"Output Feature Shape : {activation_map.shape} (Expected: (4, 6, 6))")
    print(f"ReLU Activation Sparsity: {sparsity * 100:.2f}%")