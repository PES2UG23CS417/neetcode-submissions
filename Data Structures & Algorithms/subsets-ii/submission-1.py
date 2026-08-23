class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # found = set()
        # res = []

        # def getSubsets(i, combo):
        #     if i == len(nums):
        #         if tuple(combo) not in found:
        #             found.add(tuple(combo))
        #             res.append(combo.copy())
        #         return

        #     # consider current element
        #     combo.append(nums[i])
        #     getSubsets(i+1, combo)
        #     # ignore current element
        #     combo.pop()
        #     getSubsets(i+1, combo)
        
        # getSubsets(0, [])
        # return res

        # more optimal solution
        res = []
        nums.sort()

        def backtrack(start, path):
            res.append(path.copy())

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return res