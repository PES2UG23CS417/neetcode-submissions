class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        merged = [intervals[0]]

        for interval in intervals:
            if merged[-1][1] >= interval[0]:
                merged[-1][1] = max(interval[1], merged[-1][1])
            else:
                merged.append(interval)
        
        return merged