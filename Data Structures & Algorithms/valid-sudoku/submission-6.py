class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows = collections.defaultdict(set)
        # cols = collections.defaultdict(set)
        # squares = collections.defaultdict(set)

        # for r in range(9):
        #     for c in range(9):
        #         if(board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]):
        #             return False
        #         elif(board[r][c] != "."):
        #             rows[r].add(board[r][c])
        #             cols[c].add(board[r][c])
        #             squares[(r//3, c//3)].add(board[r][c])
        # return True

        # Checking for rows
        for r in range(9):
            s = set()
            for c in range(9):
                if board[r][c] in s:
                    return False
                elif board[r][c] != ".":
                    s.add(board[r][c])
        
        for r in range(9):
            s = set()
            for c in range(9):
                if board[c][r] in s:
                    return False
                elif board[c][r] != ".":
                    s.add(board[c][r])
        
        starts = [
            (0,0), (0,3), (0,6),
            (3,0), (3,3), (3,6),
            (6,0), (6,3), (6,6)
        ]

        for i, j in starts:
            s = set()
            for r in range(i, i + 3):
                for c in range(j, j+3):
                    if board[r][c] in s:
                        return False
                    elif board[r][c] != ".":
                        s.add(board[r][c])
        
        return True