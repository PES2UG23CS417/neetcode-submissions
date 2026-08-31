class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = 0
        def isValid(mid):
            res = 0
            for p in piles:
                res += math.ceil(p/mid)
            return res <= h

        while l <= r:
            mid = (l + r)//2

            # if mid is the current eating rate
            if isValid(mid):
                k = mid
                r = mid - 1
            else:
                l = mid + 1
            
        return k
