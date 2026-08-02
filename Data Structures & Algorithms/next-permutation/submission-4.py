class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                idx = i
                break
        if idx == -1:
            # this means that the whole array is in descending order (last permutation)
            # so just reverse the array to cycle back to the first permutation
            nums.reverse()
        else:
            # swap the immediate larger element that nums[idx] with nums[idx]
            for i in range(len(nums)-1, idx, -1):
                if nums[i] > nums[idx]:
                    temp = nums[idx]
                    nums[idx] = nums[i]
                    nums[i] = temp
                    break
            # now reversing the rest of the elements after swapping
            nums[idx+1:] = nums[idx+1:][::-1]