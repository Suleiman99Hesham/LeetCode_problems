class Solution:
    def slope(self, p1, p2):
        if p2[0] - p1[0] == 0: return 'v'
        return (p2[1] - p1[1]) / (p2[0] - p1[0])
    def maxPoints(self, points) -> int:
        if len(points) == 1:
            return 1
        if len(points) == 2:
            return 2
        max_points = 0
        for i, p1 in enumerate(points[:-1]):
            slopes = {}
            for p2 in points[i+1:]:
                slope = self.slope(p1, p2)
                slopes[slope] = slopes.get(slope, 0)+1
            max_points = max(max(slopes.values())+1, max_points)
        return max_points

obj = Solution()
print(obj.maxPoints([[1,1],[2,2],[3,3]]))
print(obj.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
print(obj.maxPoints([[0,0]]))
