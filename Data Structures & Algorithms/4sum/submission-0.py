class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for a in range(n):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1, n):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                c, d = b + 1, n-1
                while c < d:
                    fourS = nums[a] + nums[b] + nums[c] + nums[d]

                    if fourS > target:
                        d -= 1
                    elif fourS < target:
                        c += 1
                    elif fourS == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        while c < d and nums[c] == nums[c-1]:
                            c += 1
        return res