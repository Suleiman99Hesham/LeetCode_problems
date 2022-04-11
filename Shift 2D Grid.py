from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        print('K:',k)
        print('m*n:',(m*n))
        print('abs:',abs((m*n)-k))
        print('abs&(m*n):',abs((m*n)-k)%(m*n))

        cut_from_index = abs((m*n)-k)%(m*n)
        if cut_from_index == 0 :
            return grid
        actual_shifts = (m*n)-cut_from_index
        shifted_one_dimensional_list = []
        for i in range(cut_from_index, m*n):
            shifted_one_dimensional_list.append(grid[i//m][i%n])
        for i in range(cut_from_index):
            shifted_one_dimensional_list.append(grid[i//m][i%n])
        result = []
        row=[]
        for i in range(m*n):
            if len(row) == m:
                result.append(row)
                row=[]
            row.append(shifted_one_dimensional_list[i])
        result.append(row)
        return result


grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]

obj = Solution()
print(obj.shiftGrid(grid,17))
print(abs(16-17)%16)
