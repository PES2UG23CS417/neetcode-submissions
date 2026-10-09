class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        for cur_amt in range(1, amount + 1):
            for coin in coins:
                if cur_amt - coin > -1:
                    dp[cur_amt] = min(dp[cur_amt], 1 + dp[cur_amt - coin])
        
        return -1 if dp[amount] >= amount + 1 else dp[amount]