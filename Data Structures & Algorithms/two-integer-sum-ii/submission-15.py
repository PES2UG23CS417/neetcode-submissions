class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # nums = [1,2,3,4]
        l, r = 0, len(numbers) - 1
        while l < r:
            res = numbers[l] + numbers[r]
            if res < target:
                l += 1
            elif res > target:
                r -= 1
            elif res == target:
                return [l+1, r+1]
