class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            l = 0
            r = n - 1

            if target > matrix[i][l] and target > matrix[i][r]:
                continue
    
            while l <= r:
                mid = (l + r)//2

                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return False