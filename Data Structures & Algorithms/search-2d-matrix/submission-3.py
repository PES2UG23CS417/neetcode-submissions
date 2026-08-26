class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # thinking of this as a sorted 1D array instead of a 2D array

        l, r = 0, (len(matrix) * len(matrix[0])) - 1
        n = len(matrix[0])

        while l <= r:
            mid = (l + r)//2
            row = mid//n
            col = mid%n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False