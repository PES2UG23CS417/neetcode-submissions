class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # this is a search problem so an efficient way to approach this would be binary search
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r)//2
            
            if nums[mid] == target:
                return mid
            
            else:
                if nums[l] <= nums[mid]:
                    # means that the left half is sorted, so we can compare those values with our target because we have a valid increasing range
                    if target < nums[l] or target > nums[mid]:
                        # shift search space to the right of mid
                        l = mid + 1
                    else:
                        # shift search space to the left of mid
                        r = mid - 1
                else:
                    # MEANS THAT THE RIght half is sorted in increasing order, so we can compare the elements in that range
                    if target < nums[mid] or target > nums[r]:
                        r = mid - 1
                    else:
                        l = mid + 1
        
        return -1