class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(len(edges) + 1)]
        
        # Helper function to check if a path exists between u and v
        def is_connected(u, v):
            q = deque([u])
            visited = set([u])

            while q:
                node = q.popleft()
                if node == v:
                    return True
                for nei in adj[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)
            return False
        
        for u, v in edges:
            # if a path already exists, this edge creates the cycle
            if is_connected(u, v):
                return [u, v]
            
            adj[u].append(v)
            adj[v].append(u)