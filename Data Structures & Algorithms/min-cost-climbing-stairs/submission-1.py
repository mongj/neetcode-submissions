class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        minA, minB = 0, 0
        for i in range(2, n+1):
            minA, minB = minB, min(minA+cost[i-2], minB+cost[i-1])
        return minB
