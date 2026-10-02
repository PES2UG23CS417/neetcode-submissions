class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        visited = set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in visited:
                return False # bc we have looped back to it
            
            if preMap[crs] == []:
                return True
            
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True