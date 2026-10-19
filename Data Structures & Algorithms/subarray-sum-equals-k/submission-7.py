class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #prefix sum must be used
        prefixSum = {0:1} # because we already have a subarray whose sum equals 0 - an empty subarray
        curSum = 0
        res = 0
        for n in nums:
            curSum += n

            if (curSum - k) in prefixSum:
                res += prefixSum[curSum - k]
            prefixSum[curSum] = prefixSum.get(curSum, 0) + 1
        
        return res