class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ele = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if(difference not in ele):
                ele[nums[i]] = i
            else:
                return [ele[difference], i]