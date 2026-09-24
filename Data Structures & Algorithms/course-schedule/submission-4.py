class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        visited = set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True
            
            # prerequisites of this crs exist, check each to see if they can be taken respectively
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            # means that all prerequisites of crs can be taken, remove crs from visited and set its prerequisites to null
            visited.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True