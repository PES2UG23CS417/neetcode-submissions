class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        for i in range(len(nums)):
            if(nums[i] not in duplicates.values()):
                print(nums[i])
                duplicates[i] = nums[i]
            else:
                print(nums[i])
                return True
        return False