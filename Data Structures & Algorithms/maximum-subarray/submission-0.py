class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        currSum = 0

        for num in nums:
            if currSum + num < num:
                # restart the subarray
                currSum = num
            else:
                # extend subarray
                currSum += num

            maxSum = max(maxSum, currSum)

        return maxSum