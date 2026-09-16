class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            intervals.append(newInterval)
        else:
            i = 0
            while i < len(intervals):
                if intervals[i][0] < newInterval[0]:
                    i += 1
                else:
                    break
            intervals.insert(i, newInterval)

        # print(intervals)
        
        res = []
        for interval in intervals:
            if res and res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        
        return res