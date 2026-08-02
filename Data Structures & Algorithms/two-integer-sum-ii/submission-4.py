class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashset={}
        for i in range(len(numbers)):
            hashset[numbers[i]] = i
        for i in range(len(numbers)-1):
            l = i
            r=len(numbers)-1
            while(l<r):
                if(numbers[l] + numbers[r] == target):
                    return [l+1, r+1]
                r -= 1
        if(0 in numbers):
            idx = (hashset[target]) + 1
            zidx = (hashset[0]) + 1
            if(zidx < idx):
                return [zidx, idx]
            else:
                return [idx, zidx]
          