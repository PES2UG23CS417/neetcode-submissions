class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, t):
            if t == len(word):
                return True
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            if board[i][j] != word[t]:
                return False
            
            temp = board[i][j]
            board[i][j] = '#'

            found = (
                dfs(i, j+1, t+1) or
                dfs(i, j-1, t+1) or
                dfs(i+1, j, t+1) or
                dfs(i-1, j, t+1)
            )

            board[i][j] = temp
            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False