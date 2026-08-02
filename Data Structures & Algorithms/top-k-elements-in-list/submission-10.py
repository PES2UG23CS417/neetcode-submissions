class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        # count = {1:1, 2:2, 3:3}
        res = []
        for n, c in count.items():
            freq[c].append(n)
        # freq = [[],[1],[2],[3],[],[]]
        for i in range(len(freq)-1,0,-1):
            for c in freq[i]:
                res.append(c)
                if len(res) == k:
                    return res