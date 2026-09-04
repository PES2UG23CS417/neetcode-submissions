class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        found = set()
        res = []

        for i in range(len(nums)):
            diff = set()
            for j in range(i+1, len(nums)):
                val = - nums[i] - nums[j]
                if val in diff:
                    if tuple(sorted([nums[i], val, nums[j]])) not in found:
                        res.append(sorted([nums[i], val, nums[j]]))
                    
                    found.add(tuple(sorted([nums[i], val, nums[j]])))
                diff.add(nums[j])
        
        return res