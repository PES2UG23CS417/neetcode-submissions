class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        pairs = {']':'[', ')':'(', '}':'{'}

        for c in s:
            if c in pairs:
                if stk and stk[-1] == pairs[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        
        if not stk:
            return True
        return False