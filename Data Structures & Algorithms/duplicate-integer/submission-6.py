class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for c in nums:
            if c in hashset:
                return True
            else:
                hashset.add(c)

        return False