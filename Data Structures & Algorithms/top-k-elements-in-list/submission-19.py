import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # min heap solution
        freq = {}
        res = []
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        min_heap = []
        
        for ele, count in freq.items():
            heapq.heappush(min_heap, (count, ele))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        for i in range(len(min_heap)):
            count, ele = heapq.heappop(min_heap)
            res.append(ele)
        
        return res