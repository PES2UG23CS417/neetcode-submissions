import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        max_heap = []

        for p in points:
            x = p[0]**2
            y = p[1]**2

            dist = math.sqrt(x + y)

            heapq.heappush(max_heap, (-dist, p))
            
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        
        return res