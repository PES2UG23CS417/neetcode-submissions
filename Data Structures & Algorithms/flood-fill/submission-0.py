class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])

        def flood(i, j, color, old):
            if i < 0 or i == m or j < 0 or j == n or image[i][j] != old:
                return

            old = image[i][j]
            image[i][j] = color

            flood(i-1, j, color, old)
            flood(i+1, j, color, old)
            flood(i, j-1, color, old)
            flood(i, j+1, color, old)

        if color == image[sr][sc]:
            return image

        flood(sr, sc, color, image[sr][sc])

        return image