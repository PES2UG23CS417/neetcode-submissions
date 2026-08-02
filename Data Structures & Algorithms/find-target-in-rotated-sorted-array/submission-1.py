class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        
        while l <= r:
            m = l + (r-l)//2
            if target == nums[m]:
                return m
            #find if left half is sorted
            if nums[m] >= nums[l]:
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else: # means that nums[m] < nums[l] [5,6,1,2,3,4]
                # means that the right half is sorted
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
