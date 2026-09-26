class Graph:
    def __init__(self, num_vertices: int, directed: bool = False):
        self.num_vertices = num_vertices
        self.directed = directed
        self.adj_list: dict[int, list[int]] = {i: [] for i in range(num_vertices)}

    def add_edge(self, u: int, v: int) -> None:
        self.adj_list[u].append(v)
        if not self.directed:
            self.adj_list[v].append(u)

    def to_adjacency_matrix(self) -> list[list[int]]:
        matrix = [[0] * self.num_vertices for _ in range(self.num_vertices)]
        for u in range(self.num_vertices):
            for v in self.adj_list[u]:
                matrix[u][v] = 1
        return matrix

    def get_degrees(self, node: int) -> dict[str, int]:
        if self.directed:
            out_degree = len(self.adj_list[node])
            in_degree = sum(node in neighbors for neighbors in self.adj_list.values())
            return {"in_degree": in_degree, "out_degree": out_degree}
        return {"degree": len(self.adj_list[node])}


if __name__ == "__main__":
    g = Graph(num_vertices=4, directed=False)
    edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
    for u, v in edges:
        g.add_edge(u, v)

    print("=== Graph Adjacency Representations ===")
    print("Adjacency List:")
    for node, neighbors in g.adj_list.items():
        print(f"  Node {node}: {neighbors}")

    print("\nAdjacency Matrix:")
    matrix = g.to_adjacency_matrix()
    for row in matrix:
        print(f"  {row}")

    print(f"\nDegrees of Node 2: {g.get_degrees(2)} (Expected: degree=3)")