class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # found = set()
        # res = []

        # for i in range(len(nums)):
        #     diff = set()
        #     for j in range(i+1, len(nums)):
        #         val = - nums[i] - nums[j]
        #         if val in diff:
        #             if tuple(sorted([nums[i], val, nums[j]])) not in found:
        #                 res.append(sorted([nums[i], val, nums[j]]))
                    
        #             found.add(tuple(sorted([nums[i], val, nums[j]])))
        #         diff.add(nums[j])
        
        # return res

        ##
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                
                if threeSum > 0:
                    # we need to reduce
                    r -= 1
                elif threeSum < 0:
                    # we need bigger values
                    l += 1
                else:
                    # threesum == 0
                    res.append([a, nums[l], nums[r]])
                    
                    # skip duplicates
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return res