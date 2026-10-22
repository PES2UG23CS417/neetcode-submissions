class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # nums = [2, 4, -3, 5]
        # res = nums[0]

        # for i in range(len(nums)):
        #     cur = nums[i]
        #     res = max(res, cur)

        #     for j in range(i + 1, len(nums)):
        #         cur *= nums[j]
        #         res = max(res, cur)
        # return res

        # optimal
        res = max(nums)

        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            temp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            res = max(res, curMax)

        return res