class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return amount
        elif len(coins) == 0:
            return -1

        dp = [[float("inf")] * (amount + 1) for _ in range(len(coins))]

        dp[0][0] = 0

        for j in range(amount + 1):
            if j - coins[0] >= 0:
                dp[0][j] = dp[0][j - coins[0]] + 1

        for i in range(1, len(coins)):
            for j in range(amount + 1):
                if j - coins[i] >= 0:
                    dp[i][j] = min(dp[i][j - coins[i]] + 1, dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        min_coins = float("inf")
        for i in range(len(coins)):
            if dp[i][amount] != -1:
                min_coins = min(min_coins, dp[i][amount])
        return min_coins if min_coins != float("inf") else -1


