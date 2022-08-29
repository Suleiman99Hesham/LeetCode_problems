class Solution:
    def majorityElement(self, nums) -> int:
        len_nums = len(nums)
        for i in nums:
            if nums.count(i) > len_nums // 2:
                return i

obj = Solution()

print(obj.majorityElement([3,2,3]))
print(obj.majorityElement([2,2,1,1,1,2,2]))
print(obj.majorityElement([6,5,5]))