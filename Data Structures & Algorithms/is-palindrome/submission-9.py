class Solution:
    def isPalindrome(self, s: str) -> bool:
        res1 = ""
        res2 = ""

        for i in s:
            if i.isalnum():
                res1 += i.lower()

        for j in range(len(s)-1, -1, -1):
            if s[j].isalnum():
                res2 += s[j].lower()
        if(res1 == res2):
            return True
        return False