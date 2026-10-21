class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def checkPal(s):
            return s == s[::-1]
        res = 0
        pal = set()
        not_pal = set()

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] in pal:
                    res += 1
                elif s[i:j+1] in not_pal:
                    continue
                elif checkPal(s[i:j+1]):
                    pal.add(s[i:j+1])
                    res += 1
                else:
                    not_pal.add(s[i:j+1])
        
        return res