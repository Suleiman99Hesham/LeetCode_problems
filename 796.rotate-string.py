#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True
        return False
# @lc code=end
