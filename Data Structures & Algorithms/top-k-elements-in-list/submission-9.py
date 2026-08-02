class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Bucket sort approach where the count is the index of the list whose len(nums)
        freq = [[] for i in range(len(nums)+1)]
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        # Now, traverse the freq array in backwards because "Top K" elements
        for i in range(len(freq)-1, 0, -1):
             for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res