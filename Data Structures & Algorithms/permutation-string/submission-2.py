class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        print(len_s1)
        s = {}
        for c in s1:
            if c not in s:
                s[c] = 1
            else:
                s[c] += 1
        print("s:", s)
        l, r = 0, 0
        t = {}
        while r < len(s2):
            while r < len(s2) and r - l + 1 <= len_s1:
                t[s2[r]] = t.get(s2[r], 0) + 1
                r += 1
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