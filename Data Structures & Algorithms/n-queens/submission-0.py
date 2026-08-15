class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."] * n for i in range(n)]
        
        def isSafe(board, row, j, n):
            # checking cols
            for i in range(n):
                if board[row][i] == "Q":
                    return False
            
            # checking rows
            for k in range(n):
                if board[k][j] == "Q":
                    return False
            
            # left diagonal
            a, b = row, j
            while a != -1 and b != -1:
                if board[a][b] == "Q":
                    return False
                a -= 1
                b -= 1
            
            a, b = row, j
            while a != -1 and b != n:
                if board[a][b] == "Q":
                    return False
                a -= 1
                b += 1
            
            return True

        def nQueens(n, row, ans, board):
            if row == n:
                ans.append(["".join(r) for r in board])
                return

            for j in range(n):
                if isSafe(board, row, j, n):
                    board[row][j] = "Q"
                    nQueens(n, row+1, ans, board)
                    board[row][j] = "."

        nQueens(n, 0, ans, board)
        return ans