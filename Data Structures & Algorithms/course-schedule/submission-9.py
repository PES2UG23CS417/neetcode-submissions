class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # BFS approach = Kahn's Algorithm - uses Topological Sorting to detect cycle
        q = deque()
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        print(adj)

        for crs, pre in prerequisites:
            indegree[crs] += 1
            adj[pre].append(crs)

        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)

        finish = 0

        while q:
            course = q.popleft()
            finish += 1
            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if finish == numCourses:
            return True
        return False