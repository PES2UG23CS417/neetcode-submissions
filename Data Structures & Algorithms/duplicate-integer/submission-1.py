class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_len = len(nums)
        nums_set = set(nums)
        set_len = len(nums_set)
        if(list_len == set_len):
            return False
        else:
            return True
        