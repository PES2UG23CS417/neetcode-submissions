class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        found = set()
        nums.sort()
        res = []

        def backtrack(start, path):
            if tuple(path) not in found:
                res.append(path.copy())
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
            
        backtrack(0, [])
        return res