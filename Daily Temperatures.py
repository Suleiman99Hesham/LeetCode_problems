class Solution:
    def dailyTemperatures(self, temperatures):
        # results = []
        # len_temperatures = len(temperatures)
        # for i in range(0, len_temperatures-1):
        #     # results.append(next((x[0] for x in enumerate(temperatures[index+1:]) if x[1] > value), -1)+1)
        #     if max(temperatures[i+1:]) < temperatures[i]:
        #         results.append(0)
        #         continue
        #     for j in range(i+1, len_temperatures):
        #         if temperatures[j] > temperatures[i]:
        #             results.append(j-i)
        #             break
        # results.append(0)
        # return results
        stack, ans = [], [0]*len(temperatures)
        
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i-cur
            stack.append(i)
        
        return ans

obj = Solution()
print(obj.dailyTemperatures([73,74,75,76,71,69,72,73]))
# print(obj.dailyTemperatures([30,40,50,60]))
# print(obj.dailyTemperatures([30,60,90]))
# print(obj.dailyTemperatures([30]))