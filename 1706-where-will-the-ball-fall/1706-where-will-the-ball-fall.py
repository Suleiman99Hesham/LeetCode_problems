class Solution:
    def findBall(self, grid):
        if len(grid[0]) == 1:
            return [-1]

        m = len(grid)
        n = len(grid[0])

        def check_path(i, j):
            if grid[i][j] == 1:
                if j == n-1:
                    return -1
                if grid[i][j+1] == -1:
                    return -1
                if i+1 == m:
                    return j+1
                return check_path(i+1, j+1)
            else:
                if j == 0:
                    return -1
                if grid[i][j-1] == 1:
                    return -1
                if i+1 == m:
                    return j-1
                return check_path(i+1, j-1)
        
        res = []
        for i in range(len(grid[0])):
            res.append(check_path(0,i))
        return res