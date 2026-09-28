def min_cost_climbing_stairs(cost: list[int]) -> int:
    first = cost[0]
    second = cost[1]

    for i in range(2, len(cost)):
        current = cost[i] + min(first, second)
        first = second
        second = current

    return min(first, second)


if __name__ == "__main__":
    stair_costs = [10, 15, 20]
    result1 = min_cost_climbing_stairs(stair_costs)
    print("=== Min Cost Climbing Stairs (O(1) Space DP) ===")
    print(f"Cost Array: {stair_costs} -> Min Cost: {result1} (Expected: 15)")

    stair_costs2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    result2 = min_cost_climbing_stairs(stair_costs2)
    print(f"Cost Array: {stair_costs2} -> Min Cost: {result2} (Expected: 6)")
    