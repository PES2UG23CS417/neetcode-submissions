class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partitions = []
        def isPalindrome(part):
            return part == part[::-1]
        
        def getAllPartitions(s, partitions):
            if len(s) == 0:
                res.append(list(partitions))

            for i in range(len(s)):
                part = s[:i+1]

                if isPalindrome(part):
                    partitions.append(part)
                    getAllPartitions(s[i+1:], partitions)
                    partitions.pop()
        
        getAllPartitions(s, partitions)
        return res