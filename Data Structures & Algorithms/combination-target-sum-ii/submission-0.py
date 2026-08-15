class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def getAllCombinations(candidates, target, idx, ans, combo):
            if target == 0:
                ans.append(list(combo))
                return
            
            if idx == len(candidates) or target < 0:
                return
            
            combo.append(candidates[idx])
            # single inclusion
            getAllCombinations(candidates, target - candidates[idx], idx + 1, ans, combo)
            # exclusion
            combo.pop()
            next_index = idx + 1
            while next_index < len(candidates) and candidates[next_index] == candidates[next_index - 1]:
                next_index += 1
            getAllCombinations(candidates, target, next_index, ans, combo)
        
        candidates.sort()
        ans = []
        combo = []

        getAllCombinations(candidates, target, 0, ans, combo)
        return ans