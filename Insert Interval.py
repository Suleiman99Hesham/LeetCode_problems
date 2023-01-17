class Solution:
    def insert(self, intervals: list, newInterval: list):
        if len(intervals) == 0:
            return [newInterval]
        dels = []
        insertion = None
        for index, curr_interval in enumerate(intervals):
            if (curr_interval[0] <= newInterval[0] <= curr_interval[1]) or (curr_interval[0] <= newInterval[1] <= curr_interval[1]) or \
                (newInterval[0] <= curr_interval[0] <= newInterval[1]) or (newInterval[0] <= curr_interval[1] <= newInterval[1]):
                newInterval = [min(curr_interval[0], newInterval[0]), max(curr_interval[1], newInterval[1])]
                dels.append(index)
            elif newInterval[1] < curr_interval[0]:
                insertion = index if len(dels) == 0 else None
                break
        if len(dels) > 0:
            if len(dels) > 1:
                del intervals[dels[0]:dels[-1]+1]
            else:
                del intervals[dels[0]]
            intervals.insert(dels[0], newInterval)
        elif insertion is not None:
            intervals.insert(insertion, newInterval)
        else:
            intervals.append(newInterval)
        return intervals

obj = Solution()
# print(obj.insert([[1,3],[6,9]], [2,5]))
# print(obj.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(obj.insert([[1,5]], [0,0]))