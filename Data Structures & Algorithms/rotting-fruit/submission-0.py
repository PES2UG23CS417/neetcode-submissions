class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        time, fresh = 0, 0
        directions = [[0,1],  [0,-1], [1,0], [-1, 0]]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append([i, j])
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    # if in vounds and fresh, make rotten
                    if (row < 0 or row == len(grid) or
                        col < 0 or col == len(grid[0]) or
                        grid[row][col] != 1):
                        continue
                    else:
                        q.append([row, col])
                        grid[row][col] = 2
                        fresh -= 1
            time += 1

        if fresh == 0:
            return time
        return -1
