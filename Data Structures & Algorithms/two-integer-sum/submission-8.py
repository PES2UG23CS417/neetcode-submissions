class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            val = target - nums[i]
            if val not in hashMap:
                hashMap[nums[i]] = i
            else:
                return [hashMap[val], i]