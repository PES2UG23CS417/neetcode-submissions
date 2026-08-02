class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        j = 0
        prod = 1
        for i in range(len(nums)):
            res[i] = prod
            prod *= nums[i]
        prod = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= prod
            prod *= nums[j]
        return res