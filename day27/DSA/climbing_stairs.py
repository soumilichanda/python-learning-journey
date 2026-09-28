def climb_stairs_memo(n: int) -> int:
    memo: dict[int, int] = {1: 1, 2: 2}

    def solve(steps: int) -> int:
        if steps in memo:
            return memo[steps]
        memo[steps] = solve(steps - 1) + solve(steps - 2)
        return memo[steps]

    return solve(n)


def climb_stairs_optimized(n: int) -> int:
    if n <= 2:
        return n
    prev2, prev1 = 1, 2
    for _ in range(3, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1


if __name__ == "__main__":
    n_steps = 5
    print("=== Climbing Stairs (DP) ===")
    print(f"Steps: {n_steps} -> Ways (Memoization): {climb_stairs_memo(n_steps)} (Expected: 8)")
    print(f"Steps: {n_steps} -> Ways (O(1) Space)  : {climb_stairs_optimized(n_steps)} (Expected: 8)")