class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        visited = set()

        def backtrack(cur, i):
            if i == n:
                # we have reached the end
                if tuple(cur) not in visited:
                    res.append(cur)
                    visited.add(tuple(cur))
                return
            
            # choose current ele
            backtrack(cur + [nums[i]], i + 1)

            # skip current ele
            backtrack(cur, i + 1)

        backtrack([], 0)
        return res