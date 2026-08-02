class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1
        
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        
        return -1