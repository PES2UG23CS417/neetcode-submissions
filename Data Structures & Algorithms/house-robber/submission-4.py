class Solution:
    def rob(self, nums: List[int]) -> int:
        house1, house2 = 0, 0

        for n in nums:
            maxRob = max(house1 + n, house2)
            house1 = house2
            house2 = maxRob
        
        return house2