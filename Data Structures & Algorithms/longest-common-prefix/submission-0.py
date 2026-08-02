class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        min_len = len(min(strs, key = len))
        l = 0

        while l < min_len:
            for i in range(1, len(strs)):
                if strs[i][l] != strs[0][l]:
                    return s
            s += strs[0][l]
            l += 1
        
        return s