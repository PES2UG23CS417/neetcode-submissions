class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 0

        def canEat(mid):
            count = 0
            for p in piles:
                count += math.ceil(p/mid)
            print("count: ", count, "k: ", mid)
            return count <= h

        while l <= r:
            mid = (l+r)//2

            if canEat(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res