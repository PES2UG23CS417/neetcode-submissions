class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # bottom up tabulation
        # coins.sort()
        # dp = [float('inf')] * (amount + 1)
        # dp[0] = 0
        # for amt in range(1, amount + 1):
        #     for coin in coins:
        #         if amt - coin < 0:
        #             break
        #         dp[amt] = min(dp[amt], 1 + dp[amt - coin])
        # print(dp)
        # return dp[amount] if dp[amount] < float('inf') else -1

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for amt in range(coin, amount + 1):
                dp[amt] = min(dp[amt], 1 + dp[amt - coin])
        
        return dp[amount] if dp[amount] < float('inf') else -1