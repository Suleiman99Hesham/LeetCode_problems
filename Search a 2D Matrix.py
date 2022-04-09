class Solution:
    def binary_search(self, arr, x):
        low = 0
        high = len(arr) - 1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                return mid
        return -1

    def searchMatrix(self, matrix, target) -> bool:
        for row in matrix:
            if row[0] > target:
                return False
            if self.binary_search(row, target) != -1:
                return True
        return False

obj=Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(obj.searchMatrix(matrix, 13))