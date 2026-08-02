class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        t = m*n
        l = 0
        r = t-1

        while l <= r:
            Mid = (l+r)//2
            i = Mid//n
            j = Mid%n

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                r = Mid - 1
            elif matrix[i][j] < target:
                l = Mid + 1
        
        return False