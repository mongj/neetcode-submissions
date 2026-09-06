class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        bestSum = float('inf')
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                currSum = nums[i] + nums[j] + nums[k]
                # terminate early if we've found the exact sum
                if currSum == target:
                    return currSum

                # update if we've found a better sum
                if abs(currSum - target) < abs(bestSum - target):
                    bestSum = currSum

                if currSum > target:
                    k -= 1
                else:
                    j += 1
        
        return bestSum