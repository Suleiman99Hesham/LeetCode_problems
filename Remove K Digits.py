import math


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        max_num=math.inf
        for i in range(len(num)-k):
            max_num = min(int(num[0:i]+num[i+k:]), max_num)
        if max_num == math.inf:
            max_num=0
        return str(max_num)

obj=Solution()
print(obj.removeKdigits("10",2))