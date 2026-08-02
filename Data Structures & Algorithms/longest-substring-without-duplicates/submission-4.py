class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        length = 0
        hashset = set()
        for r in range(len(s)):
            while s[r] in hashset:
                length -= 1
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            length += 1
            max_len = max(max_len, length)
        return max_len
