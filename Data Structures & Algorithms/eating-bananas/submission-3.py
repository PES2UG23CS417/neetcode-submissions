class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        # the above is the range of values that we can get minimum k
        def isValid(mid):
            hrs = 0
            for p in piles:
                hrs += math.ceil(p/mid)
            return hrs <= h

        while l <= r:
            mid = (l + r)//2
            if isValid(mid):
                k = mid
                r = mid - 1
            else:
                l = mid + 1

        return k