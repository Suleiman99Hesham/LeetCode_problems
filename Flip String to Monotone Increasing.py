class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        minimum_flips = float('inf')
        LHS_flips = 0
        RHS_flips = s.count('0')
        for index, char in enumerate(s):
            LHS_flips = LHS_flips + int(s[index-1]) if index > 0 else LHS_flips
            RHS_flips = RHS_flips - 1 if char == '0' else RHS_flips
            minimum_flips = min(minimum_flips, (LHS_flips + RHS_flips))
        return minimum_flips
obj = Solution()
print(obj.minFlipsMonoIncr('0'))
print(obj.minFlipsMonoIncr('010110'))
print(obj.minFlipsMonoIncr('00011000'))