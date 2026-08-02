class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Checking rows
        for r in range(9):
            s = set()
            for c in range(9):
                item = board[r][c]
                if item in s:
                    return False
                elif item != ".":
                    s.add(item)
        
        # Checking columns
        for r in range(9):
            s = set()
            for c in range(9):
                item = board[c][r]
                if item in s:
                    return False
                elif item != ".":
                    s.add(item)
        
        #Check squares
        starts = [
            (0,0), (0,3), (0,6),
            (3,0), (3,3), (3,6),
            (6,0), (6,3), (6,6)
        ]
        for i,j in starts:
            s = set()
            for r in range(i, i+3):
                for c in range(j,j+3):
                    item = board[r][c]
                    if item in s:
                        return False
                    elif item != ".":
                        s.add(item)
        return True