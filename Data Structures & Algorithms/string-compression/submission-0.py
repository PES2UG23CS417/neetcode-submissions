class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 1
        s = ""
        count = 1
        while i < len(chars):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                if count == 1:
                    s += chars[i-1]
                else:
                    s += chars[i-1] + str(count)
                count = 1
            i += 1
        
        if count == 1:
            s += chars[i-1]
        else:
            s += chars[i-1] + str(count)
        
        j = 0
        while j < len(s):
            chars[j] = s[j]
            j += 1

        for i in range(j, len(chars)):
            chars.pop(j)
        
        return len(chars)