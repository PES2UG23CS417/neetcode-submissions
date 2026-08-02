class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for i in s:
            if(i.lower().isalnum()):
                new_str += i.lower()
        print("str: ",new_str)
        rev = new_str[::-1]
        print("rev: ", rev)
        if(rev == new_str):
            return True
        return False