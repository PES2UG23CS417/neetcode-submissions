class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        dup = set()
        inSet = set()
        length = len(grid[0])

        for i in range(1, (length*length)+1):
            inSet.add(i)

        for i in range(length):
            for j in range(length):
                if grid[i][j] in dup:
                    a = grid[i][j]
                else:
                    dup.add(grid[i][j])
        b = next(iter(inSet - dup))

        return [a,b]