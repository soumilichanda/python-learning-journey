def coin_change(coins: list[int], amount: int) -> int:
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    denominations = [1, 2, 5]
    target_amount = 11
    min_coins = coin_change(denominations, target_amount)
    print("=== Minimum Coin Change (Tabulation) ===")
    print(f"Coins: {denominations}, Amount: {target_amount} -> Fewest Coins: {min_coins} (Expected: 3)")