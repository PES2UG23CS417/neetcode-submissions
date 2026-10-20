class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[float('inf')] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        # rows indicate word1 chars and cols indicate word2 chars

        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j

        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i
        
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    # 3 cases, insert, delete, replace --> all of them count as 1 operation respectively, which is why we are adding 1
                    cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])
        
        return cache[0][0]