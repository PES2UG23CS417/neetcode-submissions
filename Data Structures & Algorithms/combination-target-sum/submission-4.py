class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        found = set()
        def getAllCombos(idx, target, combo):
            if idx == len(nums) or target < 0:
                return
            
            if target == 0:
                if tuple(combo) not in found:
                    res.append(combo.copy())
                    found.add(tuple(combo))
                return
            
            combo.append(nums[idx])
            # include infinitely
            getAllCombos(idx, target - nums[idx], combo)
            # include only once
            #getAllCombos(idx + 1, target - nums[idx], combo)
            # exclude it completely
            combo.pop()
            getAllCombos(idx + 1, target, combo)
        
        getAllCombos(0, target, combo)
        return res
