class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # nums=[10, 9, 2, 5, 3, 7, 101, 18]
        LIS = [1]*len(nums)
        # LIS = [1, 1, 1, 1, 1, 1, 1, 1]
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)