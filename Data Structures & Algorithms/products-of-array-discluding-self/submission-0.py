class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0]*len(nums)
        for i in range(len(nums)):
            subarr = list(nums)
            subarr.pop(i)
            answer[i] = math.prod(subarr)
        return answer