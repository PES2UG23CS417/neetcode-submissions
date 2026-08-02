class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in hashset:
                return [hashset[val], i]
            else:
                hashset[nums[i]] = i