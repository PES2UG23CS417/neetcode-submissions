class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        
        res = []
        buckets = [[] for _ in range(len(nums) + 1)]

        for ele, count in freq.items():
            buckets[count].append(ele)

        for b in range(len(buckets) - 1, -1, -1):
            for ele in buckets[b]:
                res.append(ele)
                if len(res) == k:
                    return res