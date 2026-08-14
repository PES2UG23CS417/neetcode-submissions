class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def getAllCombinations(nums, target, idx, ans, combo):
                if len(nums) == idx or target < 0:
                    return
                if target == 0:
                    if tuple(combo) not in found:
                        found.add(tuple(combo))
                        ans.append(list(combo))
                    return
                # get the combinations -
                combo.append(nums[idx])
                # single inclusion
                getAllCombinations(nums, target - nums[idx], idx + 1, ans, combo)
                # multiple inclusion
                getAllCombinations(nums, target - nums[idx], idx, ans, combo)
                # exclusion
                combo.pop()
                getAllCombinations(nums, target, idx + 1, ans, combo)

        ans = []
        combo = []
        found = set()
        getAllCombinations(nums, target, 0, ans, combo)

        return ans