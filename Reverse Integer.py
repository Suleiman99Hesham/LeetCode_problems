class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        x_reversed = str_x[::-1]
        x = int(x_reversed) if x >= 0 else int('-'+x_reversed[:-1])
        return x if (-2**31) <= x <= (2**31) -1 else 0
obj = Solution()
print(obj.reverse(123))
print(obj.reverse(-123))
print(obj.reverse(120))
print(obj.reverse(0))
print(obj.reverse(1534236469))