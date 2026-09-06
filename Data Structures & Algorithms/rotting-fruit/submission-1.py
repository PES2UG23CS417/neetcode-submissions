class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        time, fresh = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append([i, j])

        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r+dr, c+dc

                    if row < 0 or row == m or col < 0 or col == n or grid[row][col] != 1:
                        continue
                    
                    fresh -= 1
                    grid[row][col] = 2
                    q.append([row, col])
            
            time += 1
        
        if fresh == 0:
            return time
        return -1