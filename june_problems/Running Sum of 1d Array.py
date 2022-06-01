class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i,v in enumerate(nums):
            if i == 0:
                continue
            nums[i] = nums[i-1] + v
        return nums