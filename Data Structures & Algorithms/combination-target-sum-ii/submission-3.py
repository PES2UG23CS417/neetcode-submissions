class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(idx, target, combo):
            if target == 0:
                res.append(list(combo))
                return
            
            if target < 0 or idx == len(candidates):
                return

            combo.append(candidates[idx])
            # include once
            backtrack(idx+1, target - candidates[idx], combo)

            # exclude
            combo.pop()
            next_idx = idx + 1
            while next_idx < len(candidates) and candidates[next_idx] == candidates[next_idx - 1]:
                next_idx += 1
            backtrack(next_idx, target, combo)

        backtrack(0, target, [])
        return res