import math

class Solution:
    def numsSameConsecDiff(self, n: int, k: int):
        # starting = 1*(10**(n-1))
        # res = []
        # while (int(math.log10(starting))+1) == n :
        #     flag = True
        #     for i in range(n - 1):
        #         if abs(  ((starting//(10**i))%10)  -  ((starting//(10**(i+1)))%10)  )  != k:
        #             flag = False
        #     if flag:
        #         res.append(starting)
        #     starting += 1
        # return res
        
        # BFS solution
        res = []
        q = deque((1, d) for d in range(1, 10))

        while q:
            pos, num = q.pop() # get one element
            if pos == n:    # check if we meet the length we want
                res.append(num) # we no longer need to append number if we meet the length
            else:
                for j in range(10): # loop through 0~9
                    if abs(num % 10 - j) == k:  # check if the difference between two digits is k
                        q.append((pos + 1, num * 10 + j))

        return res
