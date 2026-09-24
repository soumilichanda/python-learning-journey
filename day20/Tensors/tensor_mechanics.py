import numpy as np


class SimpleTensor:
    """A minimal pedagogical tensor demonstrating memory layout, rank, and shape."""

    def __init__(self, data: list | np.ndarray):
        self.data = np.array(data, dtype=np.float32)
        self.shape = self.data.shape
        self.strides = self.data.strides
        self.ndim = self.data.ndim
        self.device = "cpu"

    def to_device(self, target_device: str) -> "SimpleTensor":
        # Simulates hardware dispatch between execution targets
        valid_devices = ["cpu", "cuda:0", "mps"]
        if target_device not in valid_devices:
            raise ValueError(f"Unknown target device: {target_device}")
        self.device = target_device
        return self

    def __repr__(self) -> str:
        return (
            f"SimpleTensor(shape={self.shape}, rank={self.ndim}, "
            f"strides={self.strides}, device='{self.device}')\n{self.data}"
        )


if __name__ == "__main__":
    matrix_data = [
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0]
    ]

    tensor = SimpleTensor(matrix_data)
    print("=== Tensor Memory and Dimensionality Inspection ===")
    print(tensor)
    print(f"Rank (Number of Dimensions): {tensor.ndim}")
    print(f"Memory Strides (Bytes to step per axis): {tensor.strides}")

    tensor.to_device("cuda:0")
    print(f"Dispatched Device Location: {tensor.device}")