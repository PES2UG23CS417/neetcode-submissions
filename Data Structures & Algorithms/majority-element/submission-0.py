class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxDict = {}
        for i in range(len(nums)):
            if nums[i] not in maxDict:
                maxDict[nums[i]] = 1
            else:
                maxDict[nums[i]] += 1
        for i in maxDict:
            if maxDict[i] > math.floor(len(nums)/2):
                return i