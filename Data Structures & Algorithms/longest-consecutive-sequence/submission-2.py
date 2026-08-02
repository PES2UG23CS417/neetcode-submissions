class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        max_len = 0

        for i in nums:
            hashset.add(i)
        
        for i in range(len(nums)):
            length = 0
            if(nums[i] - 1 not in hashset):
                value = nums[i]
                while(value in hashset):
                    length += 1
                    value += 1
                if length > max_len:
                    max_len = length
        return max_len