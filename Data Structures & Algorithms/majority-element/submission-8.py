class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hashmap = {}
        # for n in nums:
        #     hashmap[n] = 1 + hashmap.get(n, 0)
        # sorted_dict = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        # res = list(sorted_dict.keys())
        # print(res)
        # return res[0]

        ## Most Optimal solution: Boyer Moore Algorithm
        # Time: O(n) and Space: O(1)
        res, count = nums[0], 0

        for r in range(len(nums)):
            if res != nums[r]:
                count -= 1
                if count == 0:
                    res = nums[r]
                    count += 1
            else:
                count += 1
        return res