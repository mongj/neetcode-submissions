class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        minP = prices[0]
        maxP = 0
        for i in range(n):
            minP = min(minP, prices[i])
            maxP = max(maxP, prices[i] - minP)
            
        return maxP