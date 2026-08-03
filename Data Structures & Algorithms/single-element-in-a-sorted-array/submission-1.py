class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # least optimal
        # freq = {}
        # for n in nums:
        #     freq[n] = freq.get(n, 0) + 1
        
        # for i, j in freq.items():
        #     if j == 1:
        #         return i

        # Optimal:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r-l)//2
            if (m-1 < 0 or nums[m-1] != nums[m]) and (m+1 == len(nums) or nums[m] != nums[m+1]):
                return nums[m] 
            
            leftSize = m - 1 if nums[m-1] == nums[m] else m
            if leftSize % 2 == 0:
                l = m + 1
            else:
                r = m - 1