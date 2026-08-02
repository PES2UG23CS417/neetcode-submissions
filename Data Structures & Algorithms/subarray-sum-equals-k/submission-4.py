class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum = 0
        prefixSum = {0:1}
        res = 0 # maintains the count of subarrays

        for n in nums:
            curSum += n
            diff = curSum - k
            if diff in prefixSum:
                res += prefixSum[diff]
            prefixSum[curSum] = prefixSum.get(curSum, 0) + 1

        return res