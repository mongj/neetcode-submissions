class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndices = {}
        for i, num in enumerate(nums):
            if target - num in numIndices:
                return [numIndices[target - num], i]
            numIndices[num] = i
