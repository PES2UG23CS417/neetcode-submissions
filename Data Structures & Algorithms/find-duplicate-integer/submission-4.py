class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(n) solution (not constant space) -
        # hashset = set()
        # for n in nums:
        #     if n in hashset:
        #         return n
        #     hashset.add(n)

        ## Correct sol - Floyd's Algo
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow