class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        idx = {}

        for c in range(len(s)):
            freq[s[c]] = freq.get(s[c], 0) + 1
            if s[c] not in idx:
                idx[s[c]] = c
        
        for char, f in freq.items():
            if f == 1:
                return idx[char]
        return -1