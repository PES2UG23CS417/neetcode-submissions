class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            for j in range(i + 1, len(nums)):
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
            
                # a and b are distinct values
                l, r = j + 1, len(nums) - 1
                while l < r:
                    curSum = a + nums[j] + nums[l] + nums[r]

                    if curSum < target:
                        # we need bigger values
                        l += 1
                    elif curSum > target:
                        r -= 1
                    else:
                        # curSum == target
                        print(i, j, l, r)
                        res.append([a, nums[j], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
            
        return res