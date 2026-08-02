class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp1 = ""
        for c in s:
            if str(c).isalnum():
                temp1 = temp1 + str(c).lower()
            
        temp2 = ""
        for c in range(len(s)-1, -1, -1):
            if str(s[c]).isalnum():
                temp2 = temp2 + str(s[c]).lower()
        
        if temp1 == temp2:
            return True
        else:
            return False