class Solution:
    def generate(self, numRows: int):
        result=[[1]]
        for i in range(2,numRows+1):
            row=[1,1]
            for j in range(1,i-1):
                row.insert(j,result[-1][j-1]+result[-1][j])
            result.append(row)
        return result

obj=Solution()
print(obj.generate(5))