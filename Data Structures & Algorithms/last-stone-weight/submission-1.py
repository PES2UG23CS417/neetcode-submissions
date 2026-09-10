class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) >= 2:
            st1 = heapq.heappop(stones)
            st2 = heapq.heappop(stones)

            if st1 > st2:
                heapq.heappush(stones, -(st1 - st2))
            elif st2 > st1:
                heapq.heappush(stones, -(st2 - st1))
            
        if len(stones) == 1:
            return -(heapq.heappop(stones))
        
        return 0