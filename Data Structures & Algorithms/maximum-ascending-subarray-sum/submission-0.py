class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = 0
        curSum = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] <= nums[i-1]:
                # start a new subarray
                curSum = nums[i]
            else:
                curSum += nums[i]
            maxSum = max(maxSum, curSum)
        return maxSum