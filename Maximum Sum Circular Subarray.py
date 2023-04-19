class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        len_nums = len(nums)
        if len_nums == 1:
            return nums[0]
        sums = [[None for _ in range(len_nums)] for _ in range(len_nums)]

        def get_sum(i, j):
            if i == j: return nums[i]
            curr = sums[i][j]
            if curr is None:
                curr = get_sum(i, (j - 1 + len_nums) % len_nums) + nums[j]
                sums[i][j] = curr
            return curr
        max_sum = max(nums)
        for i, num in enumerate(nums):
            j = (i + 1) % len_nums
            while i != j:
                range_sum = get_sum(i, j)
                max_sum = range_sum if range_sum > max_sum else max_sum
                j = (j + 1) % len_nums
        return max_sum

obj = Solution()
print(obj.maxSubarraySumCircular([1,-2,3,-2]))
print(obj.maxSubarraySumCircular([5,-3,5]))
print(obj.maxSubarraySumCircular([-3,-2,-3]))