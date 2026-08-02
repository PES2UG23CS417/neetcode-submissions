class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for n in nums:
            count[n] += 1
        R,W,B = count

        nums[:R] = [0]*R
        nums[R:R+W] = [1]*W
        nums[R+W:] = [2]*B