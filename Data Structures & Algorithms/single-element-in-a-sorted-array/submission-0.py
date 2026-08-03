class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # least optimal
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        for i, j in freq.items():
            if j == 1:
                return i