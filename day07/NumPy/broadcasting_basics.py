import numpy as np

if __name__ == "__main__":
    M = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    V = np.array([10, 20, 30])

    # 1. Add to each row via 1D broadcast
    row_add = M + V
    print("Row addition:\n", row_add)

    # 2. Reshape to (3, 1) to broadcast across columns
    col_add = M + V.reshape(3, 1)
    print("Column addition:\n", col_add)