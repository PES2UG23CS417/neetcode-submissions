class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1) # so that we can have amount as an index
        dp[0] = 1

        for coin in coins:
            for s in range(coin, amount + 1):
                dp[s] += dp[s-coin]
        
        return dp[amount]