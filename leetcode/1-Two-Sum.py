class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndices = {}
        n = len(nums)
        for i in range(n):
            wantNum = target - nums[i]
            if wantNum in numIndices:
                return [numIndices[wantNum], i]
            numIndices[nums[i]] = i
