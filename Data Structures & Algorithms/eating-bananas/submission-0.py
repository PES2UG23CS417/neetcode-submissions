class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = 0
        def isValid(m):
            count = 0
            for i in range(len(piles)):
                count += math.ceil(piles[i] / m)
            if count <= h:
                return True
            return False

        while l <= r:
            m = (l + r)//2
            
            if isValid(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans
