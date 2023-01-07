class Solution:
    def maxIceCream(self, costs, coins) -> int:
        if len(costs) == 1:
            return 1 if costs[0] <= coins else 0
        costs = sorted(costs)
        count = 0
        for cost in costs:
            coins -= cost
            if coins >= 0:
                count += 1
            else:
                return count
        return count