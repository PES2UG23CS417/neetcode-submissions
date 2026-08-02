class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort approach
        ele = [[] for i in range(len(nums) + 1)]
        freq = {}
        res = []
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        # i = val, j = count
        for i, j in freq.items():
            ele[j].append(i)
        
        for i in range(len(ele)-1, -1, -1):
            for j in ele[i]:
                res.append(j)
                if len(res) == k:
                    return res