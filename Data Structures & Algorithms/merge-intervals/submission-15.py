class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda i:i[0])
        res.append(intervals[0])

        for interval in intervals[1:]:
            if res[-1][1] >= interval[0]:
                # we can merge
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        
        return res