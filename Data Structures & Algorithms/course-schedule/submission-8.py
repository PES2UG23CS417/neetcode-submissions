class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # BFS approach = Kahn's Algorithm - uses Topological Sorting to detect cycle
        q = deque()
        preMap = defaultdict(list)
        indegree = [0]*numCourses

        for crs, pre in prerequisites:
            indegree[crs] += 1
            preMap[pre].append(crs)
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        finish = 0

        while q:
            node = q.popleft()
            finish += 1
            for v in preMap[node]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        return finish == numCourses