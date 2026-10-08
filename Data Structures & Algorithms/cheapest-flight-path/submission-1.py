class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        
        for u, v, price in flights:
            graph[u].append((v, price))
        
        dist = [float('inf')] * n

        # the distance to go from the src to src is 0
        dist[src] = 0

        # the queue should store the node, cost, stops so far
        q = deque([(src, 0, 0)])

        while q:
            node, cost, stops = q.popleft()

            if stops > k:
                continue
            
            for nei, wt in graph[node]:
                # cost is the lowest cost that it takes to get from the src to current node
                # wt is the cost that it is going to take from going to current the node to the nei node
                if cost + wt < dist[nei]:
                    dist[nei] = cost + wt
                    q.append((nei, dist[nei], stops + 1))
        
        return -1 if dist[dst] == float('inf') else dist[dst]