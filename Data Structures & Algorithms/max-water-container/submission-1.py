class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)-1):
            for j in range(i+1, len(heights)):
                length = min(heights[i], heights[j])
                breadth = j - i
                area = length*breadth
                max_area = max(max_area, area)

        return max_area
        