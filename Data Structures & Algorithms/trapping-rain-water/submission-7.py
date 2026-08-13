class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        leftMax = [0]*len(height)
        rightMax = [0]*len(height)
        leftMax[0] = height[0]
        rightMax[-1] = height[-1]

        for i in range(1, len(height)):
            leftMax[i] = max(height[i], leftMax[i-1])
        
        for i in range(len(height) - 2, -1, -1):
            rightMax[i] = max(height[i], rightMax[i+1])

        for i in range(len(height)):
            # print(min(leftMax[i], rightMax[i])," * 1 - ", height[i])
            val = min(leftMax[i], rightMax[i])
            res += max(val - height[i], 0)
        # print(leftMax)
        # print(rightMax)
        return res