class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Bottom Up - Tabulation
        # Time: O(Coins * Amount)
        # Space: O(amount)

        coins.sort()
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for amt in range(1, amount+1):
            for coin in coins:
                diff = amt - coin
                
                if diff < 0:
                    break
                    
                dp[amt] = min(dp[amt], 1 + dp[diff])
        
        if dp[amount] < float('inf'):
            return dp[amount]
        return -1