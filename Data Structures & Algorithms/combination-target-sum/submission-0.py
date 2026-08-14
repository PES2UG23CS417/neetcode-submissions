class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def getAllCombos(nums, idx, target, ans, combo):
            if len(nums) == idx or target < 0:
                return
            
            if target == 0:
                if tuple(combo) not in found:
                    ans.append(list(combo))
                    found.add(tuple(combo))
                return

            combo.append(nums[idx])
            # single
            getAllCombos(nums, idx+1, target - nums[idx], ans, combo)
            # multiple
            getAllCombos(nums, idx, target - nums[idx], ans, combo)
            # exclude
            combo.pop()
            getAllCombos(nums, idx+1, target, ans, combo)
        
        ans = []
        combo = []
        found = set()

        getAllCombos(nums, 0, target, ans, combo)

        return ans