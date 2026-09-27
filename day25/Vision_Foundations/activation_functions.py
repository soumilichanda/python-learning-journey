import numpy as np


class ReLU:
    def __init__(self):
        self.cache = None

    def forward(self, x: np.ndarray) -> np.ndarray:
        self.cache = x
        return np.maximum(0.0, x)

    def backward(self, dout: np.ndarray) -> np.ndarray:
        dx = dout.copy()
        dx[self.cache <= 0.0] = 0.0
        return dx


class LeakyReLU:
    def __init__(self, alpha: float = 0.01):
        self.alpha = alpha
        self.cache = None

    def forward(self, x: np.ndarray) -> np.ndarray:
        self.cache = x
        return np.where(x > 0.0, x, x * self.alpha)

    def backward(self, dout: np.ndarray) -> np.ndarray:
        dx = dout.copy()
        dx[self.cache <= 0.0] *= self.alpha
        return dx


if __name__ == "__main__":
    inputs = np.array([-2.5, -0.5, 0.0, 1.2, 3.4], dtype=np.float32)
    upstream_grad = np.ones_like(inputs)

    relu_layer = ReLU()
    out = relu_layer.forward(inputs)
    grad = relu_layer.backward(upstream_grad)

    print("=== Vectorized Non-Linear Activations ===")
    print(f"Inputs   : {inputs}")
    print(f"ReLU Out : {out}")
    print(f"ReLU Grad: {grad}")
    