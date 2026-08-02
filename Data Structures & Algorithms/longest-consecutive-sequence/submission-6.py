class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        maxLen = 0
        hashset = set(nums)
        for i in range(len(nums)):
            if nums[i] - 1 not in hashset:
                length = 1
                while nums[i] + length in hashset:
                    length += 1
                maxLen = max(maxLen, length)

        return maxLen