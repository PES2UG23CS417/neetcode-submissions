class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            # because some x + nums[i] = target and if we already found x, then we have stored in visited already
            if diff in visited:
                return [visited[diff], i]
            
            else:
                visited[nums[i]] = i