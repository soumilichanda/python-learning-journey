def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    adj: list[list[int]] = [[] for _ in range(num_courses)]
    for dest, src in prerequisites:
        adj[src].append(dest)

    # 0 = Unvisited, 1 = Visiting, 2 = Visited
    state = [0] * num_courses

    def has_cycle(course: int) -> bool:
        if state[course] == 1:
            return True  # Encountered back-edge into active stack: Cycle detected
        if state[course] == 2:
            return False  # Subtree already evaluated and acyclic

        state[course] = 1
        for nxt in adj[course]:
            if has_cycle(nxt):
                return True

        state[course] = 2
        return False

    for c in range(num_courses):
        if state[c] == 0:
            if has_cycle(c):
                return False

    return True


if __name__ == "__main__":
    print("=== Course Schedule Directed Cycle Detection ===")
    print(f"Can finish [[1, 0]]: {can_finish(2, [[1, 0]])} (Expected: True)")
    print(f"Can finish [[1, 0], [0, 1]]: {can_finish(2, [[1, 0], [0, 1]])} (Expected: False)")