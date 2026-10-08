class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('inf')] * n
        graph = [[] for _ in range(n)]

        for u, v, prices in flights:
            graph[u].append((v, prices))

        print(graph)

        q = deque([(src, 0, -1)])

        while q:
            node, cost, stops = q.popleft()

            if stops == k:
                continue
            print(dist)
            for nei, wt in graph[node]:
                if cost + wt < dist[nei]:
                    dist[nei] = cost + wt
                    q.append((nei, dist[nei], stops + 1))
        print(dist)
        return -1 if dist[dst] == float('inf') else dist[dst]