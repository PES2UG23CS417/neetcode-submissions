class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = {}
        t = {}
        for c in s1:
            s[c] = s.get(c, 0) + 1
        t_len = len(s2)
        s_len = len(s1)
        l, r = 0, 0
        while r < t_len:
            while r < t_len and r - l + 1 <= s_len:
                t[s2[r]] = t.get(s2[r], 0) + 1
                r += 1
            print("s:", s)
            print("t:", t)
            if s == t:
                return True
            else:
                if t[s2[l]] == 1:
                    t.pop(s2[l])
                else:
                    t[s2[l]] -= 1
                l += 1
        return False