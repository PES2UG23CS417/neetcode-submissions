class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashset = collections.defaultdict(list)
        for i in range(len(numbers)):
            hashset[numbers[i]].append(i+1)
        for i in range(len(numbers)):
            diff = target - numbers[i] 
            if (diff in hashset):
                if(min(hashset[diff]) < max(hashset[numbers[i]])):
                    return [min(hashset[diff]), max(hashset[numbers[i]])]
                else:
                    return [min(hashset[numbers[i]]), min(hashset[diff])]
          