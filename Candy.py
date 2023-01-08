class Solution:
    def count(self, n):
        return n*(n+1)/2
    def candy(self, ratings):
        if len(ratings) <= 1:
            return len(ratings)
        candies = up = down = old_slope = 0
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                new_slope = 1
            elif ratings[i] < ratings[i-1]:
                new_slope = -1
            else:
                new_slope = 0
            if ((old_slope > 0 and new_slope == 0) or (old_slope < 0 and new_slope >= 0)):
                candies += self.count(up) + self.count(down) + max(up, down)
                up = down = 0
            if new_slope > 0:
                up += 1
            elif new_slope < 0:
                down += 1 
            else:
                candies += 1
            old_slope = new_slope
        candies += self.count(up) + self.count(down) + max(up, down) + 1
        return int(candies)
obj = Solution()
print(obj.candy([1,0,2]))
print(obj.candy([1,2,2]))
print(obj.candy([1,3,2,2,1]))
print(obj.candy([1,3,4,5,2]))


    # def compute_window(self, window):
    #     diff = [1]
    #     for i in range(1,len(window)):
    #         if window[i-1] > window[i]:
    #             diff.append(diff[i-1] - 1)
    #         elif window[i-1] < window[i]:
    #             diff.append(diff[i-1] + 1)
    #         else:
    #             if i == 1 and window[i+1] < window[i]:
    #                 diff.append(diff[i-1]+1)
    #             elif i == 2 and window[i-2] < window[i]:
    #                 diff.append(diff[i-2])
    #             else:
    #                 diff.append(diff[i-1])
    #     m = 1 - min(diff)
    #     return list(map(lambda x: x+m, diff))

    # def candy(self, ratings):
    #     diffs = [0 for i in ratings]
    #     for i in range(1,len(ratings)-1):
    #         computed_window = self.compute_window(ratings[i-1:i+2])
    #         diffs[i-1] = max(diffs[i-1], computed_window[0])
    #         diffs[i] = max(diffs[i], computed_window[1])
    #         diffs[i+1] = max(diffs[i+1], computed_window[2])
    #     return sum(diffs)