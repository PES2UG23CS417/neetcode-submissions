class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        s_dict = {}
        t_dict = {}
        for letter in range(len(s)):
            if(s[letter] not in s_dict):
                s_dict[s[letter]] = 1
            else:
                s_dict[s[letter]] += 1

            if(t[letter] not in t_dict):
                t_dict[t[letter]] = 1
            else:
                t_dict[t[letter]] += 1
        if(s_dict == t_dict):
            return True
        return False
        