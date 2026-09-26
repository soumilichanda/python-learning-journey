def find_center(edges: list[list[int]]) -> int:
    # The center node must be shared by the first two edges
    edge1, edge2 = edges[0], edges[1]
    return edge1[0] if edge1[0] in edge2 else edge1[1]


if __name__ == "__main__":
    test_edges = [[1, 2], [2, 3], [4, 2]]
    center = find_center(test_edges)
    print("=== Center of Star Graph ===")
    print(f"Edges: {test_edges} -> Center Node: {center} (Expected: 2)")