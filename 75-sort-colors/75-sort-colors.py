class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        reds = 0
        whites = 0
        blues = 0
        for num in nums:
            reds += 1 if num == 0 else 0
            whites += 1 if num == 1 else 0
            blues += 1 if num == 2 else 0
        for i, v in enumerate(nums):
            if reds > 0:
                nums[i] = 0
                reds -= 1
            elif whites > 0:
                nums[i] = 1
                whites -= 1
            elif blues > 0:
                nums[i] = 2
                blues -= 1