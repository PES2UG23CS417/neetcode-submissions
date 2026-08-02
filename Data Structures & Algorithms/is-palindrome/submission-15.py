class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        string = ""
        for i in range(len(s)):
            if s[i].isalnum():
                string += s[i].lower()
        l, r = 0, len(string) - 1
        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True