class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # charSet = set()
        # maxL = 0
        # l = 0
        # for r in range(len(s)):
        #     while s[r] in charSet:
        #         charSet.remove(s[l])
        #         l += 1
        #     charSet.add(s[r])
        #     maxL = max(maxL, r - l + 1)
        # return maxL

        visited = set()
        maxLen = 0
        l = 0
        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen