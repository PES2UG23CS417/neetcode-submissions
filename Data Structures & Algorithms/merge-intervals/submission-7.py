class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        merged = [intervals[0]]

        for start, end in intervals[1:]:
            if merged[-1][1] >= start:
                merged[-1][1] = max(end, merged[-1][1])
            else:
                merged.append([start, end])
        
        return merged