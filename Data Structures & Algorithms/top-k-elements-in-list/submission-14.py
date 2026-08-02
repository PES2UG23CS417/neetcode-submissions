class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        # count = {1:1, 2:2, 3:3} {num:count}
        buckets = [[] for i in range(len(nums) + 1)]
        res = []
        for i,j in count.items():
            buckets[j].append(i)
        for i in range(len(buckets)-1, -1, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res