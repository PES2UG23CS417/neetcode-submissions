class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      visited = {}

      for i in range(len(nums)):
        value = target - nums[i]

        if value in visited:
            return [visited[value], i]

        visited[nums[i]]   = i