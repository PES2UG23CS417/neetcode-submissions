class Solution:
    def isPalindrome(self, s: str) -> bool:
        # l, r = 0, len(s) - 1
        # string = ""
        # for i in range(len(s)):
        #     if s[i].isalnum():
        #         string += s[i].lower()
        # l, r = 0, len(string) - 1
        # while l < r:
        #     if string[l] != string[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True

        l, r = 0, len(s) - 1
        while l < r:
            while(l < r and not s[l].isalnum()):
                l += 1
            while (r > l and not s[r].isalnum()):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True