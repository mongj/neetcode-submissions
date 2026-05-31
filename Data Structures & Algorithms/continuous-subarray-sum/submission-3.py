class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prefixSum = [0] * n
        for i in range(n):
            prefixSum[i] = prefixSum[i - 1] + nums[i]
        seen = {0: -1}
        for i, ps in enumerate(prefixSum):
            rem = ps % k
            if rem in seen:
                if i - seen[rem] > 1:
                    return True
            else:
                seen[rem] = i
        return False
