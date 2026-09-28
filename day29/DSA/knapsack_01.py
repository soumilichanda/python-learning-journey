def knapsack_01(weights: list[int], values: list[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        w = weights[i]
        v = values[i]
        # Iterate backwards to ensure each item is considered at most once
        for cap in range(capacity, w - 1, -1):
            dp[cap] = max(dp[cap], dp[cap - w] + v)

    return dp[capacity]


if __name__ == "__main__":
    item_weights = [1, 3, 4, 5]
    item_values = [1, 4, 5, 7]
    bag_capacity = 7

    max_val = knapsack_01(item_weights, item_values, bag_capacity)
    print("=== 0/1 Knapsack (Space-Optimized DP) ===")
    print(f"Weights : {item_weights}")
    print(f"Values  : {item_values}")
    print(f"Capacity: {bag_capacity}")
    print(f"Max Value Achievable: {max_val} (Expected: 9)")