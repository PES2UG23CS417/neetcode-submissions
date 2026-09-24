class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = defaultdict(list)
        visited = set()
        adj = [[] for _ in range(numCourses)]

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            adj[pre].append(crs)
        
        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True
            
            # check neighbors
            visited.add(crs)
            for node in preMap[crs]:
                if not dfs(node):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True