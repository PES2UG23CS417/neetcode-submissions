class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort approach
        freq = [[] for i in range(len(nums) + 1)]
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        # count =  {1:1, 2:2, 3:3}
        for i, j in count.items():
            freq[j].append(i)
        
        # get the k most freq elements
        res = []
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res