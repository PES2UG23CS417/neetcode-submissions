class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # if 1 not in nums:
        #     return 1
        # else:
        #     nums.sort()
        #     i = 0
            
        #     while nums[i] != 1:
        #         i += 1
        #     res = 1
        #     while i < len(nums)-1 and nums[i] == nums[i+1]:
        #         i += 1
        #     while i < len

        ## Correct solution
        n = len(nums)
        i = 0
        while i < n:
            correct = nums[i]-1
            if (1 <= nums[i] <= n and nums[i] != nums[correct]):
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1