class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            ele1 = -heapq.heappop(stones)
            ele2 = -heapq.heappop(stones)

            if ele1 > ele2:
                heapq.heappush(stones, -(ele1 - ele2))
            elif ele2 > ele1:
                heapq.heappush(stones, -(ele2 - ele1))
        
        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0