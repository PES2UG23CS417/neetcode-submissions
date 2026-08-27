class Solution:
    def trap(self, height: List[int]) -> int:
        # res = 0
        # leftMax = [0]*len(height)
        # rightMax = [0]*len(height)
        # leftMax[0] = height[0]
        # rightMax[-1] = height[-1]

        # for i in range(1, len(height)):
        #     leftMax[i] = max(height[i], leftMax[i-1])
        
        # for i in range(len(height) - 2, -1, -1):
        #     rightMax[i] = max(height[i], rightMax[i+1])

        # for i in range(len(height)):
        #     # print(min(leftMax[i], rightMax[i])," * 1 - ", height[i])
        #     val = min(leftMax[i], rightMax[i])
        #     res += max(val - height[i], 0)
        # # print(leftMax)
        # # print(rightMax)
        # return res

        # ## Above solution optimized for space -
        # if not height:
        #     return 0
        
        # l, r = 0, len(height) - 1
        # leftMax, rightMax = height[l], height[r]
        # res = 0

        # while l < r:
        #     if leftMax < rightMax:
        #         # we know that leftMax is the bottleneck
        #         res += leftMax - height[l]
        #         l += 1
        #         leftMax = max(leftMax, height[l])
        #     else:
        #         res += rightMax - height[r]
        #         r -= 1
        #         rightMax = max(rightMax, height[r])

        # return res

        ## repeat
        leftMax = [0]*len(height)
        rightMax = [0]*len(height)
        leftMax[0] = height[0]
        rightMax[-1] = height[-1]
        res = 0
        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i-1], height[i])
        for i in range(len(height)-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])
        for i in range(len(height)):
            res += (min(leftMax[i], rightMax[i]) - height[i])
        
        return res