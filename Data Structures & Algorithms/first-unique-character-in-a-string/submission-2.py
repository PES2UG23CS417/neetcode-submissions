class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        for idx, ch in enumerate(s):
            if freq[ch] == 1:
                return idx
        
        return -1