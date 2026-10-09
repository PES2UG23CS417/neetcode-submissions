class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap, self.k = nums, k
        heapq.heapify(self.heap)
        # only maintain a min heap with the k largest elements. so if the len of the heap is greater than k, we are going to keep deleting all the min elements until we are left with the kth largest elements. therefore the kth largest element is going to be the minimum most element in the heap of k elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]