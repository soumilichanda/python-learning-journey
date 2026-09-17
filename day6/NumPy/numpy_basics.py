import numpy as np

def run_numpy_basics():
    # 1. 1D Array Inspection
    arr = np.array([10, 20, 30, 40, 50])
    print("Array:", arr)
    print("Number of dimensions:", arr.ndim)
    print("Size:", arr.size)
    print("Data type:", arr.dtype)
    print("First element:", arr[0])
    print("Last element:", arr[-1])

    # 2. Reshaping Exercises
    grid = np.arange(1, 13)
    
    matrix_3x4 = grid.reshape(3, 4)
    print("\nReshaped 3x4:\n", matrix_3x4)
    
    matrix_4x3 = grid.reshape(4, 3)
    print("\nReshaped 4x3:\n", matrix_4x3)

if __name__ == "__main__":
    run_numpy_basics()