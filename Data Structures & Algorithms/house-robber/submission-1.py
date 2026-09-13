class Solution:
    def rob(self, nums: List[int]) -> int:
        maxA, maxB = 0, 0
        for i in range(len(nums)):
            maxA, maxB = maxB, max(maxA + nums[i], maxB)
        return maxB
