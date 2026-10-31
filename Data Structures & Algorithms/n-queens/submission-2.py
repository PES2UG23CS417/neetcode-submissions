class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        res = []

        def isValid(board, r, c):
            # check the row
            for i in range(c):
                if board[r][i] == "Q":
                    return False

            # check the col
            for i in range(r):
                if board[i][c] == "Q":
                    return False
            
            # check left upper diagonal
            a, b = r, c
            while a != -1 and b != -1:
                if board[a][b] == "Q":
                    return False
                a -= 1
                b -= 1

            # check upper right diagonal
            a, b = r, c
            while a != -1 and b != n:
                if board[a][b] == "Q":
                    return False
                a -= 1
                b += 1

            return True

        def nQueens(board, r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if isValid(board, r, c):
                    board[r][c] = "Q"
                    nQueens(board, r + 1)
                    board[r][c] = "."
                    
        nQueens(board, 0)
        return res