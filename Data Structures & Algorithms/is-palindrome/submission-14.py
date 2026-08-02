class Solution:
    def isPalindrome(self, s: str) -> bool:
        # temp1 = ""
        # for c in s:
        #     if str(c).isalnum():
        #         temp1 = temp1 + str(c).lower()
            
        # temp2 = ""
        # for c in range(len(s)-1, -1, -1):
        #     if str(s[c]).isalnum():
        #         temp2 = temp2 + str(s[c]).lower()
        
        # if temp1 == temp2:
        #     return True
        # else:
        #     return False

        ## 2 Points solution
        l, r = 0, len(s) - 1
        while l < r:
            while s[l].isalnum() == False and l < r:
                l += 1

            while s[r].isalnum() == False and l < r:
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
                
        return True