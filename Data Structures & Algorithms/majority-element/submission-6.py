class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = nums[0], 1
        for i in range(1, len(nums)):
            print("nums[i] = ", nums[i], "res =", res)
            if(nums[i] == res):
                count += 1
                print("count = ", count)
            else:
                count -= 1
                print("count = ", count)
                if (count == 0 or count < 0):
                    res = nums[i]
        return res