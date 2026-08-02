class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxA = 0
        while l < r:
            area = min(height[l], height[r]) * (r-l)
            maxA = max(area, maxA)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxA