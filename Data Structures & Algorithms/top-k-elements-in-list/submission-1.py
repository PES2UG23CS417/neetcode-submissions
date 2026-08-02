class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        res = []
        for i in nums:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] += 1
        # valueList = list(frequency.values())
        # valueList.sort(reverse = True)

        # for j in range(k):
        #     for key, value in frequency.items():
        #         if value == valueList[j]:
        #             res.append(key)
        new_freq = dict(sorted(frequency.items(), key = lambda item: item[1], reverse = True))
        keyList = list(new_freq.keys())
        for j in range(k):
            res.append(keyList[j])
        
        return res
