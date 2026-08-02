class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'}':'{', ')':'(', ']':'['}

        # for i in range(len(s)):
        #     if s[i] == '(' or s[i] == '{' or s[i] == '[':
        #         stack.append(s[i])
        #     else:
        #         if stack and stack[-1] == pairs[s[i]]:
        #             stack.remove(stack[-1])
        #         elif stack and pairs[s[i]] != stack[-1]:
        #             return False
        #         else:
        #             return False
        # if not stack:
        #     return True
        # else:
        #     return False

        for c in s:
            if c in pairs:
                if stack and pairs[c] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(c)

        if not stack:
            return True
        else:
            return False