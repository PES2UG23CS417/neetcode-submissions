class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        maxlen = 0
        for i in range(len(nums)):
            hashset.add(nums[i])

        for i in range(len(nums)):
            length = 0
            if((nums[i] - 1) not in hashset):
                value = nums[i]
                while(value in hashset):
                    length += 1
                    value += 1
                if(length > maxlen):
                    maxlen = length
        return maxlen

        # [2,20,4,10,3,4,5]
        # set = {2,20,4,10,3,5}
        """"
        value = 2
        len = 1, val = 3
        len=2, val = 4
        len=3, val=5
        len=4, val=6
        """