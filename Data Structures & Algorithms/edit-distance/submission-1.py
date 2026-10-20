class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        cache = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        # all columns of last row
        for j in range(n + 1):
            cache[m][j] = n - j
        
        # update all rows of last column
        for i in range(m + 1):
            cache[i][n] = m - i

        print(cache)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])
        
        return cache[0][0]