class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for u, v, price in flights:
            graph[u].append((v, price))
        
        dist = [float('inf')] * n

        q = deque([(src, 0, 0)]) # (node, cost, stops)

        while q:
            node, cost, stops = q.popleft()
            if stops > k:
                continue
            for nei, wt in graph[node]:
                if cost + wt < dist[nei]:
                    dist[nei] = cost + wt
                    q.append((nei, dist[nei], stops + 1))
        return -1 if dist[dst] == float('inf') else dist[dst]