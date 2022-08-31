class Solution:
    def twoSum(self, numbers, target):
        remain ={}
        for idx, value in enumerate(numbers):
            if (target-value) in remain:
                return list((remain[target-value]+1, idx+1))
            else: remain[value] = idx