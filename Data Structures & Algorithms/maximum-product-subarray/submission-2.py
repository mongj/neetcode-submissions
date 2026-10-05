class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        globalMax = float('-inf')
        currMax, currMin = 1, 1

        for num in nums:
            currMax, currMin = max(currMax * num, currMin * num, num), min(currMax * num, currMin * num, num)
            globalMax = max(globalMax, currMax)

        return globalMax