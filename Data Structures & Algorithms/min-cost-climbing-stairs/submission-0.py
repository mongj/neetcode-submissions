class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        minCosts = [0] * (n+1)
        for i in range(2, n+1):
            minCosts[i] = min(minCosts[i-1]+cost[i-1], minCosts[i-2]+cost[i-2])
        return minCosts[-1]
