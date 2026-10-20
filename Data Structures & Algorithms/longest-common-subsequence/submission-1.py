class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # recursive approach (brute force)
        # def LCS(i, j):
        #     if i == len(text1) or j == len(text2):
        #         return 0
            
        #     elif text1[i] == text2[j]:
        #         return 1 + LCS(i+1, j+1)
            
        #     else:
        #         return max(LCS(i+1, j), LCS(i, j+1))
        
        # return LCS(0, 0)

        # memoization in recursion approach
        m, n = len(text1), len(text2)
        memo = {}

        def LCS(i, j):
            if i == m or j == n:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            elif text1[i] == text2[j]:
                memo[(i, j)] = 1 + LCS(i+1, j+1)
            
            else:
                memo[(i, j)] = max(LCS(i, j+1), LCS(i+1, j))
            
            return memo[(i, j)]
        
        return LCS(0, 0)