class Solution:
    def merge(self, intervals : list[int]):
        i = 0
        intervals = sorted(intervals, key=lambda x: x[0])
        while i < len(intervals)-1:
            if max(intervals[i+1][0], intervals[i][0]) <= min(intervals[i+1][1], intervals[i][1]):
                intervals[i][0] = min(intervals[i+1][0], intervals[i][0])
                intervals[i][1] = max(intervals[i+1][1], intervals[i][1])
                del intervals[i+1]
                continue
            i += 1
        return intervals