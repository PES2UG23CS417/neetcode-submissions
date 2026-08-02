class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        res = 0
        hashset = set()
        
        for c in s:
            while c in hashset:
                hashset.remove(s[l])
                l += 1
            res = max(res, r - l)
            hashset.add(c)
            r += 1
        return res