class Solution:
    def trap(self, height: List[int]) -> int:
        value = [0]*len(height)
        for i in range(len(height)):
            temp1 = height[0:i]
            temp2 = height[i+1:]
            
            if not temp1:
                l = 0
            else:
                l = max(temp1)
            if not temp2:
                r = 0
            else:
                r = max(temp2)
            val = min(l, r) - height[i]
            if val < 0:
                value[i] = 0
            else:
                value[i] = val
        
        return sum(value)
