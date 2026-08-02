class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l,r = 0, 1
        while r < len(prices):
            while r < len(prices) and prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
                r += 1
            l = r
            r += 1
        return maxP