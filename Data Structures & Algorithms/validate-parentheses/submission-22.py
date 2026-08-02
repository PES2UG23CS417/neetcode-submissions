class Solution:
    def isValid(self, s: str) -> bool:
        match = {'}':'{', ')':'(', ']':'['}
        stack = []
        for c in s:
            if c in match:
                if stack and match[c] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        
        return False