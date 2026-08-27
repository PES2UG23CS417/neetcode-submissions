class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        UP_WALL = 0
        RIGHT_WALL = len(matrix[0])
        LEFT_WALL = -1
        DOWN_WALL = len(matrix)
        length = (len(matrix)*len(matrix[0]))
        res = []
        direction = "RIGHT"
        i = 0
        j = 0
        while True:
            if direction == "RIGHT":
                while j != RIGHT_WALL:
                    res.append(matrix[i][j])
                    j += 1
                if len(res) == length:
                    return res
                direction = "DOWN"
                i, j = i + 1, j-1
                RIGHT_WALL -= 1
            
            if direction == "DOWN":
                while i != DOWN_WALL:
                    res.append(matrix[i][j])
                    i += 1
                if len(res) == length:
                    return res
                direction = "LEFT"
                i, j = i-1, j-1
                DOWN_WALL -= 1

            if direction == "LEFT":
                while j != LEFT_WALL:
                    res.append(matrix[i][j])
                    j -= 1
                if len(res) == length:
                    return res
                LEFT_WALL += 1
                i, j = i - 1, j + 1
                direction = "UP"
            
            if direction == "UP":
                while i != UP_WALL:
                    res.append(matrix[i][j])
                    i -= 1
                if len(res) == length:
                    return res
                i, j = i + 1, j + 1
                direction = "RIGHT"
                UP_WALL += 1