class Solution:
    def canJump(self, nums: List[int]) -> bool:
        flag = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= flag:
                flag = i
        
        if flag == 0:
            return True
        return False