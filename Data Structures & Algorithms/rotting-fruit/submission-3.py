class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh, time = 0, 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append([i, j])

        directions = [[0,1], [0,-1], [-1,0], [1,0]]
        
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = (row + dr), (col + dc)
                    if r < 0 or r == m or c < 0 or c == n or grid[r][c] != 1:
                        continue 
                    fresh -= 1
                    grid[r][c] = 2
                    q.append([r, c])
            time += 1
        
        if fresh == 0:
            return time
        return -1