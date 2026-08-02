class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort approach
        res = [[] for i in range(len(nums) + 1)] 
        result =  []
        # +1 to accomodate the 
        # frequency being equal to the length of nums
        # For eg: [3, 3, 3] k
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        # freq = {1: 1, 2: 2, 3: 3}
        # values = count of the key
        for n, c in freq.items():
            res[c].append(n)
        for i in range(len(res)-1, 0, -1):
            for j in res[i]:
                result.append(j)
                if len(result) == k:
                    return result