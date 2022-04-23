from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        if k >= (m*n):
            actual_shifts = abs((m*n)-k)%(m*n)
        else:
            actual_shifts = k
        if actual_shifts == 0 :
            return grid
        cut_from_index = (m*n)-actual_shifts
        shifted_one_dimensional_list = []
        for i in range(cut_from_index, m*n):
            x,y = i//m, i%n
            shifted_one_dimensional_list.append(grid[x][y])
        for i in range(cut_from_index):
            shifted_one_dimensional_list.append(grid[i//m][i%n])
        result = []
        row=[]
        for i in range(m*n):
            if len(row) == n:
                result.append(row)
                row=[]
            row.append(shifted_one_dimensional_list[i])
        result.append(row)
        return result


grid = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]


obj = Solution()
print(obj.shiftGrid(grid,2))
print('1//3:', 1//3)
print('3//1:', 3//1)
print('3//3:', 3//3)
print('1%3:', 1%3)
print('3%1:', 3%1)
print('3%3:', 3%3)
