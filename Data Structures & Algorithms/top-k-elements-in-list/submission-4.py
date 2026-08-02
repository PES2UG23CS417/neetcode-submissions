class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        new_dict = dict(sorted(freq.items(), key = lambda item: item[1]))
        res_key = list(new_dict.keys())
        ptr = len(res_key) - 1
        while(k!=0):
            k -= 1
            res.append(res_key[ptr])
            ptr -= 1
        return res
