class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False
        s, t = {}, {}
        for i in range(n1):
            s[s1[i]] = s.get(s1[i], 0) + 1
            t[s2[i]] = t.get(s2[i], 0) + 1
        
        if s == t:
            return True
        
        for i in range(n1, n2):
            t[s2[i-n1]] -= 1
            if t[s2[i-n1]] == 0:
                del t[s2[i-n1]]
            t[s2[i]] = t.get(s2[i], 0) + 1

            if s == t:
                return True
        
        return False