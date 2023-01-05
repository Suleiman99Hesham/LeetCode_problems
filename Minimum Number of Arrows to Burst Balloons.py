class Solution:
    def findMinArrowShots(self, points) -> int:
        if len(points) == 1:
            return 1
        points_sorted = sorted(points)
        idx = 0
        range = (points_sorted[0][0], points_sorted[0][1])
        arrows = 1
        for point in points_sorted:
            if range[0] <= point[0] <= range[1]:
                range = (max(range[0], point[0]), min(range[1], point[1]))
            else:
                arrows += 1
                range = (point[0], point[1])
        return arrows
                


obj = Solution()
print(obj.findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))