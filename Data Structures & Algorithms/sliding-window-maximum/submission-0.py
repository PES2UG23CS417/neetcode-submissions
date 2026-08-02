class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = []

        for r in range(len(nums)):
            window.append(nums[r])
            if len(window) == k:
                res.append(max(window))
                window.pop(0)
        return res