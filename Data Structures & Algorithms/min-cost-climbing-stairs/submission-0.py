class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        if len(cost) == 2: 
            return min(cost[0], cost[1])

        prev = cost[1]
        prev2 = cost[0]
        for i in range(2, len(cost)): 
            curr = cost[i] + min(prev, prev2)
            prev2 = prev
            prev = curr 
        return min(prev, prev2)