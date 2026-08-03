class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        merged = [intervals[0]]

        for interval in intervals:
            if merged[-1][1] >= interval[0]:
                # means we can merge because overlap
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
        
        return merged