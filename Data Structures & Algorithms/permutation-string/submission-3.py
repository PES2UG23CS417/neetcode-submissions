class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = {}
        t = {}

        for c in s1:
            s[c] = s.get(c, 0) + 1
        l, r = 0, 0
        while r < len(s2):
            while r < len(s2) and r - l + 1 <= len(s1):
                t[s2[r]] = t.get(s2[r], 0) + 1
                r += 1
            if s == t:
                return True
            else:
                if t[s2[l]] == 1:
                    t.pop(s2[l])
                else:
                    t[s2[l]] -= 1
                l += 1
        
        return False