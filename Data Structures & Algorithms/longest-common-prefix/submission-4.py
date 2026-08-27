class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = 0
        min_len = len(min(strs))
        while l < min_len:
            for s in strs:
                if s[l] != strs[0][l]:
                    return s[0:l]
            l += 1
        return strs[0][0:l]