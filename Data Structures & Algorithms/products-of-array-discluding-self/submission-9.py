class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        res = []

        for n in nums:
            res.append(prefix)
            prefix *= n
        
        prefix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= prefix
            prefix *= nums[i]
        
        return res