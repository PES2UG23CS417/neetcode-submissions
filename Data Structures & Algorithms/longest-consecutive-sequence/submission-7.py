class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        i = 0
        maxLen = 0
        while i < len(nums):
            if nums[i] - 1 not in hashSet:
                length = 1
                while nums[i] + length in hashSet:
                    length += 1
                maxLen = max(maxLen, length)
            i += 1
        return maxLen
            