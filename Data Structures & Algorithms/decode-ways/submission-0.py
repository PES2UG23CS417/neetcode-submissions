class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:
                # either i is already cached or it is the last position in the string
                return dp[i]
            # if it is not end of string
            if s[i] == "0":
                return 0
            
            # that means it is between 1 - 9
            res = dfs(i + 1)
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                # then we can take a double digit value as well
                res += dfs(i + 2)
            dp[i] = res

            return res
        
        return dfs(0)