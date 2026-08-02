class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices = [10,8,7,5,2]
        l,r = 0,1
        maxP = 0
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            r += 1
        return maxP