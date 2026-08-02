class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]

        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        res = []
        for n, c in count.items():
            # n - key, c - val
            freq[c].append(n)
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        