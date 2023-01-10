class Solution:
    def minDeletionSize(self, strs) -> int:
        count = 0
        for i in range(len(strs[0])):
            col = []
            for str in strs:
                col.append(str[i])
            count += 1 if col != sorted(col) else 0
        return count

obj = Solution()