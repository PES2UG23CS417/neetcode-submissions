class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(i, dots, curPath):
            if dots == 4:
                if i == len(s):
                    res.append(curPath[:-1])
                return    
            # if not, all dots have not been put yet, so continue

            for j in range(i, min(i+3, len(s))):
                if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"):
                    backtrack(j + 1, dots + 1, curPath + s[i:j+1] + ".")
        
        backtrack(0, 0, "")
        return res