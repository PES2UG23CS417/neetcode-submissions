class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n-1
        leftMax = height[l]
        rightMax = height[r]
        res = 0
        if not height:
            return 0

        while l<r:
            if leftMax <= rightMax:
                val = leftMax - height[l]
                if val > 0:
                    res += val
                l += 1
                leftMax = max(leftMax, height[l])

            elif rightMax < leftMax:
                val = rightMax - height[r]
                if val > 0:
                    res += val
                r -= 1
                rightMax = max(rightMax, height[r])
        return res
            