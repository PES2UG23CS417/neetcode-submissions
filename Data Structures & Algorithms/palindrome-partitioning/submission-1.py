class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []

        def isPalin(s):
            return s == s[::-1]

        def getPartitions(s, combo):
            if len(s) == 0:
                res.append(list(combo))
                return
            
            for i in range(len(s)):
                if isPalin(s[0:i+1]):
                    combo.append(s[0:i+1])
                    getPartitions(s[i+1:], combo)
                    combo.pop()
        getPartitions(s, [])
        return res
