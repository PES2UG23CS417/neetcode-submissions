class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # most optimal - using a min heap
        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                heapq.heappushpop(heap, num)
                # or in 2 lines do -
                # heapq.heappush(heap, num)
                # heapq.heappop(heap)
        
        return heapq.heappop(heap)