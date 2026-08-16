class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def getAllCombos(idx, target, combo):
            if target == 0:
                res.append(list(combo))
                return

            if idx == len(candidates) or target < 0:
                return
            
            combo.append(candidates[idx])
            getAllCombos(idx+1, target - candidates[idx], combo)
            combo.pop()
            next_idx = idx + 1
            while next_idx < len(candidates) and candidates[next_idx] == candidates[next_idx - 1]:
                next_idx += 1
            getAllCombos(next_idx, target, combo)
        
        getAllCombos(0, target, [])
        return res
        
