class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        if sum(gas) < sum(cost):
            return -1        
        tank = idx = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                idx = i + 1
        return idx
obj = Solution()
print(obj.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
print(obj.canCompleteCircuit([2,3,4], [3,4,3]))
print(obj.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]))