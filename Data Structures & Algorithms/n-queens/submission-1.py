class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]
        
        def isValid(board, r, c):
            # checking row
            for i in range(n):
                if board[r][i] == "Q":
                    return False

            #checking column
            for i in range(r):
                if board[i][c] == "Q":
                    return False

            # checking left upper diagonal
            a, b = r, c
            while a != -1 and b != -1:
                if board[a][b] == "Q":
                    return False
                a -= 1
                b -= 1
            
            # checking right upper diagonal
            a,b = r, c
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
                # c is the col where queen could be placed 
                if isValid(board, r, c):
                    board[r][c] = "Q"
                    nQueens(board, r+1)
                    board[r][c] = "."
        nQueens(board, 0)
        return res