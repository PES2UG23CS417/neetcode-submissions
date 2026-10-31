class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        left, right = 0, n - 1

        while left < right:
            top, bottom = left, right
            for i in range(right - left):
                # storing topleft in a var
                topLeft = matrix[top][left + i]

                # move bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # move bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # move top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # move top left to top right
                matrix[top + i][right] = topLeft
            left += 1
            right -= 1