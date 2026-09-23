def combine(n: int, k: int) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []

    def backtrack(start: int) -> None:
        if len(path) == k:
            result.append(list(path))
            return

        need = k - len(path)
        for i in range(start, n - need + 2):
            path.append(i)
            backtrack(i + 1)
            path.pop()

    backtrack(1)
    return result


if __name__ == "__main__":
    n_val, k_val = 4, 2
    combs = combine(n_val, k_val)
    print(f"Combinations for n={n_val}, k={k_val} (Total: {len(combs)}):")
    print(combs)