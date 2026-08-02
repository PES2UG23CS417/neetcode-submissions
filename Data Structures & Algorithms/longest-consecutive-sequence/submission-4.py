class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_len = 0
        for n in nums:
            if (n - 1 not in numSet):
                # this means that n is the starting point
                length = 0
                while (n + length in numSet):
                    length += 1
                max_len = max(max_len, length)

        return max_len