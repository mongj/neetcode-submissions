class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndices = {}
        for i, num in enumerate(nums):
            wantNum = target - num
            if wantNum in numIndices:
                return [numIndices[wantNum], i]
            numIndices[num] = i