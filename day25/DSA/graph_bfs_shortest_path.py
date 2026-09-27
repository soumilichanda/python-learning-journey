from collections import deque


def bfs_shortest_path(graph: dict[int, list[int]], start: int, target: int) -> tuple[int, list[int]]:
    if start == target:
        return 0, [start]

    visited = {start}
    queue: deque[int] = deque([start])
    parent: dict[int, int] = {start: None}

    while queue:
        curr = queue.popleft()

        if curr == target:
            break

        for neighbor in graph.get(curr, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = curr
                queue.append(neighbor)

    if target not in parent:
        return -1, []

    # Reconstruct path by following parent pointers backward
    path = []
    step = target
    while step is not None:
        path.append(step)
        step = parent[step]
    path.reverse()

    return len(path) - 1, path


if __name__ == "__main__":
    # Graph adjacency list
    adj = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3, 4],
        3: [1, 2, 5],
        4: [2, 5],
        5: [3, 4]
    }

    dist, shortest_p = bfs_shortest_path(adj, start=0, target=5)
    print("=== BFS Shortest Path ===")
    print(f"Distance: {dist} edges (Expected: 3)")
    print(f"Path    : {shortest_p}")