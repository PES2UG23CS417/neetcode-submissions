class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []
        # UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
        direction = "RIGHT"
        i, j = 0, 0
        UP_WALL = 0
        DOWN_WALL = m
        RIGHT_WALL = n
        LEFT_WALL = -1 
        while len(res) != m*n:
            if direction == "RIGHT":
                while j < RIGHT_WALL:
                    res.append(matrix[i][j])
                    j += 1
                i, j = i + 1, j - 1
                direction = "DOWN"
                RIGHT_WALL -= 1

            elif direction == "DOWN":
                while i  < DOWN_WALL:
                    res.append(matrix[i][j])
                    i += 1
                i, j = i - 1, j - 1
                DOWN_WALL -= 1
                direction = "LEFT"
            
            elif direction == "LEFT":
                while j > LEFT_WALL:
                    res.append(matrix[i][j])
                    j -= 1
                i, j = i-1, j+1
                LEFT_WALL += 1
                direction = "UP"
            
            elif direction == "UP":
                while i > UP_WALL:
                    res.append(matrix[i][j])
                    i -= 1
                UP_WALL += 1
                i, j = i+1, j+1
                direction = "RIGHT"

        return res