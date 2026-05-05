class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxP = 0
        for i in range(n - 1):
            for j in range(i, n):
                maxP = max(maxP, prices[j] - prices[i])
            
        return maxP