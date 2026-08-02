class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        res = []

        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            freq[c].append(n)
        for j in range(len(freq) - 1, 0, -1):
            for c in freq[j]:
                res.append(c)
                if len(res) == k:
                    return res;