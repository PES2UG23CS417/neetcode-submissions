class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # nums = [1,1,1], k = 2
        res = 0
        prefixSums = {0:1}
        curSum = 0

        for n in nums:
            curSum += n
            diff = curSum - k
            if diff in prefixSums:
                res += prefixSums[diff]
            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1
        
        return res