class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

        for i in range(len(self.nums)):
            self.nums[i] = -self.nums[i]

        heapq.heapify(self.nums)

    def add(self, val: int) -> int:
        visited = []

        heapq.heappush(self.nums, -val)

        for i in range(self.k - 1):
            visited.append(heapq.heappop(self.nums))
        
        res = heapq.heappop(self.nums)

        while visited:
            heapq.heappush(self.nums, visited.pop())
        heapq.heappush(self.nums, res)
        return -res