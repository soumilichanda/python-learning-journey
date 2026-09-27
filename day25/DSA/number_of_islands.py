from collections import deque


def num_islands(grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    def bfs(r_start: int, c_start: int) -> None:
        queue = deque([(r_start, c_start)])
        grid[r_start][c_start] = "0"  # Mark as visited in-place

        while queue:
            r, c = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    grid[nr][nc] = "0"
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                bfs(r, c)

    return islands


if __name__ == "__main__":
    sample_grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    print("=== Number of Islands (2D Grid BFS) ===")
    print(f"Discovered Islands: {num_islands(sample_grid)} (Expected: 3)")