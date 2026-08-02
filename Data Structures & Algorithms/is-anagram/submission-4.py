class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_let = {}
        t_let = {}
        if(len(s) == len(t)):
            for i in range(len(s)):
                if(s[i] not in s_let):
                    s_let[s[i]] = 1
                else:
                    s_let[s[i]] += 1
                if(t[i] not in t_let):
                    t_let[t[i]] = 1
                else:
                    t_let[t[i]] += 1
            print(s_let)
            print(t_let)
            if(s_let == t_let):
                return True
            else:
                return False
        else:
            return False

        