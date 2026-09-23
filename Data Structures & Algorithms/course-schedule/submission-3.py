class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(set)
        visited = set()

        for i, j in prerequisites:
            preMap[i].add(j)
        
        def dfs(node):
            if node in visited:
                return False
            if len(preMap[crs]) == 0:
                return True
            
            visited.add(node)
            for pre in preMap[node]:
                if not dfs(pre): return False
            visited.remove(node)
            preMap[node] = set()
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True