class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        for i in range(0, len(nums)):
            if (i -1 < 0 or nums[i] != nums[i-1]) and (i + 1 == len(nums) or nums[i] != nums[i+1]):
                return nums[i]