class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = ['' for i in range(numRows)]
        counter, increase = 0, 1
        for char in s:
            rows[counter] += char
            counter += increase
            if counter == numRows:
                counter -= 2
                increase = -1
            elif counter < 0:
                counter = 1
                increase = 1
        return ''.join(rows)

obj = Solution()
print(obj.convert('PAYPALISHIRING', 3))