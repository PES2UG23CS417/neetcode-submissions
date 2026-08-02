class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        length = 0
        maxlen = 0
        hashset = set()

        for r in range(len(s)):
            while s[r] in hashset:
                length -= 1
                hashset.remove(s[l])
                l += 1

            hashset.add(s[r])
            length += 1
            maxlen = max(maxlen, length)
        return maxlen