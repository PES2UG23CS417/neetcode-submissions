class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)
        sorted_dict = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        res = list(sorted_dict.keys())
        print(res)
        return res[0]