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

        maxL = 0
        hashset = set()
        r = 0
        l = 0
        for c in s:
            while c in hashset:
                hashset.remove(s[l])
                l += 1
                
            hashset.add(c)
            r += 1
            maxL = max(maxL, r-l)
        return maxL