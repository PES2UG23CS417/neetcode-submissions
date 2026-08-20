class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPali(part):
            return part == part[::-1]

        def getAllPartitions(s, combo):
            if len(s) == 0:
                res.append(combo.copy())
                return
            
            for i in range(len(s)):
                part = s[0:i+1]
                
                if isPali(part):
                    combo.append(part)
                    getAllPartitions(s[i+1:], combo)
                    combo.pop()
        getAllPartitions(s, [])
        return res