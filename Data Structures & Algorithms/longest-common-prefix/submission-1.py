class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        l = 0
        min_len = len(min(strs))
        while l < min_len:
            for i in range(1, len(strs)):
                if strs[i][l] != strs[0][l]:
                    return res
            res += strs[0][l]
            l += 1
        return res           