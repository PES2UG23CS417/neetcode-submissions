class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        q = deque()
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] += 1
        
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)

        finish = 0

        while q:
            
            crs = q.popleft()
            finish += 1
            res.append(crs)

            for nei in graph[crs]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if finish == numCourses:
            return res
        return []