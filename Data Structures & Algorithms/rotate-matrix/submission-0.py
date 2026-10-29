class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        
        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save the topleft value
                topLeft = matrix[top][l + i]

                # move the bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into the bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move original top left into top right
                matrix[top + i][r] = topLeft

            # now, update the pointers
            l += 1
            r -= 1