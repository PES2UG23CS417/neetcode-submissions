class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        ref = s.replace(" ", "")
        string = ref.strip("?!.',@#$%^&*()_-/;:+=<>|")
        new_str = ""
        for i in range(len(ref)):
            if(ref[i].isalnum()):
                new_str += ref[i]
        rev = new_str[::-1]
        print("str:"+new_str)
        print("rev:"+rev)
        if(rev == new_str):
            return True
        return False