class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l <= r:
            m = l + (r - l)//2

            if nums[m] == target:
                return m

            if nums[m] >= nums[l]: # means that the left half is sorted [2,3,4,5,1]
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else: # means that the right half is sorted [5,6,1,2,3,4]
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1