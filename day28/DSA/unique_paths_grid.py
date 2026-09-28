def unique_paths(m: int, n: int) -> int:
    # Initialize rolling row with 1s (base case: only one way to move along top row)
    row = [1] * n

    for _ in range(m - 1):
        curr_row = [1] * n
        for j in range(1, n):
            curr_row[j] = curr_row[j - 1] + row[j]
        row = curr_row

    return row[-1]


if __name__ == "__main__":
    rows, cols = 3, 7
    total_paths = unique_paths(rows, cols)
    print("=== Unique Paths (2D DP Rolling Space) ===")
    print(f"Grid: {rows}x{cols} -> Unique Paths: {total_paths} (Expected: 28)")