class Solution:
    def matrixReshape(self, mat, r, c):
        m=len(mat)
        n=len(mat[0])
        if m*n == r*c:
            result=[]
            row=[]
            for i in range(m*n):
                row.append(mat[i//n][i%n])
                if (i+1)%c == 0:
                    result.append(row[:])
                    row.clear()
            return result
        else:
            return mat

mat = [[1,2],[3,4]]
r = 2
c = 4
obj=Solution()
print(obj.matrixReshape(mat, r,c))

# m_n=[[2,4,6],[8,10,12]]
# r_c=[[2,4],[6,8],[10,12]]
# m=len(m_n)
# n=len(m_n[0])
# r=n
# c=m
# for i in range(m*n):
#     row=[]
#     if (r_c[i//c][i%c] == m_n[i//n][i%n]):
#         print(True)
#     else: print(False)


# print(0%4)
# print(1%4)
# print(2%4)
# print(3%4)
# print(4%4)