class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c in closeToOpen: 
                # checks if c is present in the dict as a key 
                # if it is, then it is close bracket
                if (stack and stack[-1] == closeToOpen[c]):
                    stack.pop(-1)
                else:
                    return False
            else:
            #this means that it is an open bracket in which case we push into stack
                stack.append(c)
        if not stack:
            return True
        else:
            return False
