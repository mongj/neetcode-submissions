class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        totalProfit = 0
        hasShare = False
        currentBoughtPrice = 0

        for i, price in enumerate(prices):
            # buy if nexy day is higher
            if not hasShare and i < len(prices) - 1 and prices[i + 1] > price:
                currentBoughtPrice = price
                hasShare = True

            # skip buy if next day is lower because we can alwaysbuy then

            # sell if next element is smaller or last element
            if hasShare and (i == len(prices) - 1 or prices[i + 1] < price):
                totalProfit += price - currentBoughtPrice
                currentBoughtPrice = 0
                hasShare = False

        return totalProfit