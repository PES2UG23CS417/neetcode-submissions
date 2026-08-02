class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]
        for j in range(len(nums)-1, -1, -1):
            res[j] *= postfix 
            postfix *= nums[j]
        return res
            