class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        count = 0

        for r in range(len(nums)):
            if res != nums[r]:
                count -= 1
                if count == 0:
                    res = nums[r]
                    count += 1
            else:
                count += 1
        
        return res