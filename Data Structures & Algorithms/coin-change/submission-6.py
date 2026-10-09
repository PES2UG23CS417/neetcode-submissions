class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # top down solution
        coins.sort()
        memo = {0:0}

        def minCoins(amt):
            if amt in memo:
                return memo[amt]
            minn =   float('inf')
            for coin in coins:
                diff = amt - coin
                
                if diff < 0:
                    break
                minn = min(minn, 1 + minCoins(diff))
            memo[amt] = minn
            return minn
        
        minCoins(amount)
        return memo[amount] if memo[amount] < float('inf') else -1