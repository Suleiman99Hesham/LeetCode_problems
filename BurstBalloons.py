from copy import deepcopy

class Solution:
    def __init__(self):
        self.max_value = 0

    def maxCoins(self, nums) -> int:
        array_size = len(nums)
        nums.insert(0,1)
        nums.append(1)
        db_Matrix = [[0 for x in range(array_size+2)] for y in range(array_size+2)]
        for window in range(1,array_size+1):
            for left in range(1,array_size-window+2):
                right = left+window-1
                for i in range(left,right+1):
                    db_Matrix[left][right]=max(db_Matrix[left][right], (nums[left-1]*nums[i]*nums[right+1]) + (db_Matrix[left][i-1]+db_Matrix[i+1][right]))
        return db_Matrix[1][array_size]

    

object = Solution()
list=[35,16,83,87,84,59,48,41,20,54]
max=object.maxCoins(list)
print(max)