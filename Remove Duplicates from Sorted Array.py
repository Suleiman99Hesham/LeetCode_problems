class Solution:
    def removeDuplicates(self, nums) -> int:
        len_nums = len(nums)
        if len_nums == 1:
            return 1
        i, j = 0, 1
        while True:
            if nums[j] > nums[i]:
                nums[i+1], nums[j] = nums[j], nums[i+1]
                i, j = i+1, j+1
            else:
                j+=1
            if j >= len_nums:
                return i+1