class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # BFS Approach  = Kahn's algorithm
        # indegree = [0] * numCourses
        # adj = [[] for _ in range(numCourses)]
        # q = deque()

        # for crs, prereq in prerequisites:
        #     # the edge is going to be directed from the prereq to the crs
        #     indegree[crs] += 1
        #     adj[prereq].append(crs)
        
        # for node in range(len(indegree)):
        #     if indegree[node] == 0:
        #         q.append(node)

        # finish = 0
            
        # while q:
        #     node = q.popleft()
        #     finish += 1
        #     # decrease all the indegrees of its neighbors
        #     for v in adj[node]:
        #         indegree[v] -= 1
        #         if indegree[v] == 0:
        #             q.append(v)

        # return finish == numCourses

        ## repeat of Kahn's Algorithm - Topological sorting
        indegree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        q = deque()

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            indegree[crs] += 1
        
        for crs in range(numCourses):
            if indegree[crs] == 0:
                q.append(crs)
        
        finish = 0

        while q:
            course = q.popleft()
            finish += 1
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if finish == numCourses:
            return True
        return False