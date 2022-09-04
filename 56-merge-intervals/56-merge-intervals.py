class Solution:
    def merge(self, intervals : list[int]):
        i = 0
        intervals = sorted(intervals, key=lambda x: x[0])
        while i < len(intervals)-1:
            print(intervals[i+1][0], intervals[i][0], intervals[i+1][1], intervals[i][1])
            print(max(intervals[i+1][0], intervals[i][0]) , min(intervals[i+1][1], intervals[i][1]))
            if max(intervals[i+1][0], intervals[i][0]) <= min(intervals[i+1][1], intervals[i][1]):
                intervals[i][0] = min(intervals[i+1][0], intervals[i][0])
                intervals[i][1] = max(intervals[i+1][1], intervals[i][1])
                del intervals[i+1]
                continue
            i += 1
        return intervals


print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge([[1,4],[0,4]]))
print(Solution().merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))