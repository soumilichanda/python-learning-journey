def count_components(n: int, edges: list[list[int]]) -> tuple[int, list[list[int]]]:
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited: set[int] = set()
    components: list[list[int]] = []

    def dfs(node: int, comp: list[int]) -> None:
        visited.add(node)
        comp.append(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                dfs(neighbor, comp)

    for vertex in range(n):
        if vertex not in visited:
            current_component: list[int] = []
            dfs(vertex, current_component)
            components.append(current_component)

    return len(components), components


if __name__ == "__main__":
    n_nodes = 6
    edge_list = [[0, 1], [1, 2], [3, 4]]
    # Component 1: {0, 1, 2}, Component 2: {3, 4}, Component 3: {5} (isolated)

    total_comps, groups = count_components(n_nodes, edge_list)
    print("=== Connected Components via DFS ===")
    print(f"Total Components: {total_comps} (Expected: 3)")
    print(f"Discovered Groups: {groups}")