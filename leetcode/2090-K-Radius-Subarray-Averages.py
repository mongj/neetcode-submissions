class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        lastSum = None
        for i in range(k, n - k):
            if lastSum:
                newSum = lastSum + nums[i + k] - nums[i - k - 1]
            else:
                newSum = 0
                for j in range(i - k, i + k + 1):
                    newSum += nums[j]
            lastSum = newSum
            res[i] = newSum // (2 * k + 1)
        return res