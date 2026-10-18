class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        if len(s) > 12:
            return res
        
        def backtrack(i, dots, curPath):
            if dots == 4:
                if i == len(s):
                    res.append(curPath[:-1])
                return
            
            for j in range(i, min(i+3, len(s))):
                # i represents the start index, j represents the current index
                if int(s[i:j+1]) < 256 and (j == i or s[i] != "0"):
                    backtrack(j+1, dots + 1, curPath + s[i:j+1] + ".")
        
        backtrack(0, 0, "")
        return res