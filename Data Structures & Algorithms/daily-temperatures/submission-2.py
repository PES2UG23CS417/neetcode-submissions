class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        # we want a monotonically descreasing stack so anytime we encounter a greater temperature, which is what we want, we compare the indices of the current higher temp and the lower temp present in the stack and subtract because that is the result that we want
        res = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while stk and temperatures[i] > stk[-1][0]:
                idx = stk.pop()[1]
                days = i - idx
                res[idx] = days
            stk.append([temperatures[i], i])
        
        return res